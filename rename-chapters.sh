#!/usr/bin/env bash
# rename-chapters.sh
#
# Renames chapter markdown files in a target directory to NN-kebab-case-title.md
# where NN is the two-digit chapter number derived from the file's H1 heading
# and the title is the H1 lowercased with the rules:
#   - "Chapter N —/–/-/:" prefix stripped
#   - "Epilogue —/–/-/:" prefix stripped
#   - lowercased
#   - "&" → " and "
#   - em (—) / en (–) dashes and colons (:) deleted
#   - spaces → hyphens
#   - non-[a-z0-9-] chars removed
#   - multiple hyphens collapsed
#   - leading/trailing hyphens trimmed
#
# Special rules:
#   - 00-frontmatter.md (literal filename) is not renamed.
#   - A file whose H1 starts with "Epilogue" gets the next number after
#     the highest chapter number found.
#   - Files with no H1 or an H1 that doesn't match "Chapter N" or "Epilogue"
#     are moved to <chapters_dir>/_unresolved/.
#   - If two files resolve to the same NN, the newer (by mtime) keeps the
#     target name and the older is moved to _unresolved/.
#   - Nothing is deleted. If a target name already exists at the destination,
#     the script reports it and skips that move.
#
# Usage:
#   ./rename-chapters.sh [chapters_dir]   # defaults to ./chapters
#
# Requires bash 4+ (macOS system bash is 3.2 — install via `brew install bash`).

set -euo pipefail

if (( BASH_VERSINFO[0] < 4 )); then
    echo "Error: bash 4+ required (you have $BASH_VERSION)." >&2
    echo "On macOS:  brew install bash" >&2
    echo "Then run:  /opt/homebrew/bin/bash $0   (or /usr/local/bin/bash on Intel)" >&2
    exit 1
fi

CHAPTERS_DIR="${1:-chapters}"

if [[ ! -d "$CHAPTERS_DIR" ]]; then
    echo "Error: directory '$CHAPTERS_DIR' not found." >&2
    echo "Usage: $0 [chapters_dir]" >&2
    exit 1
fi

UNRESOLVED_DIR="$CHAPTERS_DIR/_unresolved"
mkdir -p "$UNRESOLVED_DIR"

# ----- helpers -----

# Extract first H1 line (content after "# "), ignoring "##" or higher.
extract_h1() {
    awk '/^# [^#]/ { sub(/^# +/, ""); sub(/[[:space:]]+$/, ""); print; exit }' "$1"
}

# Extract chapter number from H1; empty if no match.
extract_chapter_num() {
    local h1="$1"
    if [[ "$h1" =~ [Cc]hapter[[:space:]]+([0-9]{1,3}) ]]; then
        echo "${BASH_REMATCH[1]}"
    fi
}

# Detect epilogue.
is_epilogue() {
    [[ "$1" =~ ^[[:space:]]*[Ee]pilogue ]]
}

# Slugify per the spec.
slugify() {
    local s="$1"
    # Strip "Chapter N —/–/-/:" prefix (with optional separator)
    s=$(printf '%s' "$s" | sed -E 's/^[Cc]hapter[[:space:]]+[0-9]+[[:space:]]*[—–:-][[:space:]]*//')
    # Strip "Epilogue —/–/-/:" prefix
    s=$(printf '%s' "$s" | sed -E 's/^[Ee]pilogue[[:space:]]*[—–:-][[:space:]]*//')
    # Lowercase
    s=$(printf '%s' "$s" | tr '[:upper:]' '[:lower:]')
    # & → " and "
    s=$(printf '%s' "$s" | sed 's/&/ and /g')
    # Drop em (—), en (–) dashes, and colons
    s=$(printf '%s' "$s" | sed 's/[—–:]//g')
    # Spaces → hyphens
    s=$(printf '%s' "$s" | tr ' ' '-')
    # Drop everything except a-z, 0-9, hyphen
    s=$(printf '%s' "$s" | LC_ALL=C tr -cd 'a-z0-9-')
    # Collapse multi-hyphens
    s=$(printf '%s' "$s" | sed -E 's/-+/-/g')
    # Trim leading/trailing hyphens
    s=$(printf '%s' "$s" | sed -E 's/^-+|-+$//g')
    printf '%s' "$s"
}

# Cross-platform mtime (macOS BSD stat or GNU stat).
file_mtime() {
    if stat -f %m "$1" 2>/dev/null; then return; fi
    stat -c %Y "$1"
}

# Move that refuses to overwrite.
safe_mv() {
    local src="$1" dst="$2"
    if [[ "$src" == "$dst" ]]; then
        return 0
    fi
    if [[ -e "$dst" ]]; then
        echo "  SKIP (target exists): $(basename "$src") → $(basename "$dst")" >&2
        return 1
    fi
    mv "$src" "$dst"
}

# ----- pass 1: gather files & metadata -----

declare -a all_files=()
declare -A file_h1=()
declare -A file_status=()    # FRONTMATTER | CHAPTER:N | EPILOGUE | UNRESOLVED:reason
declare -A file_slug=()

while IFS= read -r -d '' f; do
    all_files+=("$f")
done < <(find "$CHAPTERS_DIR" -maxdepth 1 -type f -name '*.md' -print0 | sort -z)

max_chapter=0

for f in "${all_files[@]}"; do
    bn=$(basename "$f")

    if [[ "$bn" == "00-frontmatter.md" ]]; then
        file_status["$f"]="FRONTMATTER"
        continue
    fi

    h1=$(extract_h1 "$f")
    file_h1["$f"]="$h1"

    if [[ -z "$h1" ]]; then
        file_status["$f"]="UNRESOLVED:no H1 heading"
        continue
    fi

    num=$(extract_chapter_num "$h1")
    if [[ -n "$num" ]]; then
        n=$((10#$num))
        file_status["$f"]="CHAPTER:$n"
        file_slug["$f"]=$(slugify "$h1")
        if (( n > max_chapter )); then max_chapter=$n; fi
    elif is_epilogue "$h1"; then
        file_status["$f"]="EPILOGUE"
        file_slug["$f"]=$(slugify "$h1")
    else
        file_status["$f"]="UNRESOLVED:H1 not parseable as Chapter N or Epilogue (\"${h1:0:80}\")"
    fi
done

# Resolve epilogue numbers (now that we know max_chapter).
epilogue_num=$((max_chapter + 1))
for f in "${all_files[@]}"; do
    if [[ "${file_status[$f]:-}" == "EPILOGUE" ]]; then
        file_status["$f"]="CHAPTER:$epilogue_num"
    fi
done

# ----- pass 2: detect collisions on NN -----

declare -A num_to_files=()   # NN → "file1\nfile2\n..." (newline-delimited)

for f in "${all_files[@]}"; do
    status="${file_status[$f]}"
    case "$status" in
        FRONTMATTER|UNRESOLVED:*) continue ;;
    esac
    n="${status#CHAPTER:}"
    nn=$(printf "%02d" "$n")
    if [[ -n "${num_to_files[$nn]:-}" ]]; then
        num_to_files["$nn"]="${num_to_files[$nn]}"$'\n'"$f"
    else
        num_to_files["$nn"]="$f"
    fi
done

declare -A keepers=()              # NN → file (the one that gets the target name)
declare -A files_to_unresolve=()   # file → reason

for nn in "${!num_to_files[@]}"; do
    # Read newline-delimited file list into an array.
    files_arr=()
    while IFS= read -r line; do
        [[ -n "$line" ]] && files_arr+=("$line")
    done <<< "${num_to_files[$nn]}"

    if (( ${#files_arr[@]} == 1 )); then
        keepers["$nn"]="${files_arr[0]}"
        continue
    fi

    # Multiple files for same NN — keep newest by mtime, unresolve the rest.
    newest=""
    newest_mt=0
    for cf in "${files_arr[@]}"; do
        mt=$(file_mtime "$cf")
        if (( mt > newest_mt )); then
            newest_mt=$mt
            newest="$cf"
        fi
    done
    keepers["$nn"]="$newest"
    for cf in "${files_arr[@]}"; do
        if [[ "$cf" != "$newest" ]]; then
            files_to_unresolve["$cf"]="collision at $nn — newer file kept: $(basename "$newest")"
        fi
    done
done

# Add files that were UNRESOLVED from pass 1.
for f in "${all_files[@]}"; do
    status="${file_status[$f]}"
    if [[ "$status" == UNRESOLVED:* ]]; then
        files_to_unresolve["$f"]="${status#UNRESOLVED:}"
    fi
done

# ----- pass 3: execute -----

echo "=== Renaming chapters in $CHAPTERS_DIR ==="
echo

# Frontmatter (always unchanged, but report it).
for f in "${all_files[@]}"; do
    if [[ "${file_status[$f]}" == "FRONTMATTER" ]]; then
        echo "Unchanged (frontmatter): $(basename "$f")"
    fi
done
echo

# Move unresolved.
if (( ${#files_to_unresolve[@]} > 0 )); then
    echo "Moved to _unresolved/:"
    for f in "${!files_to_unresolve[@]}"; do
        bn=$(basename "$f")
        reason="${files_to_unresolve[$f]}"
        if safe_mv "$f" "$UNRESOLVED_DIR/$bn"; then
            echo "  $bn  →  _unresolved/$bn"
            echo "      reason: $reason"
        fi
    done
    echo
fi

# Rename keepers.
if (( ${#keepers[@]} > 0 )); then
    echo "Renamed:"
    # Sort by NN for nicer output.
    while IFS= read -r nn; do
        f="${keepers[$nn]}"
        slug="${file_slug[$f]:-untitled}"
        target_bn="${nn}-${slug}.md"
        target_path="$CHAPTERS_DIR/$target_bn"
        src_bn=$(basename "$f")
        if [[ "$src_bn" == "$target_bn" ]]; then
            echo "  $src_bn  (already correct)"
        else
            if safe_mv "$f" "$target_path"; then
                echo "  $src_bn  →  $target_bn"
            fi
        fi
    done < <(printf '%s\n' "${!keepers[@]}" | sort)
    echo
fi

# ----- final ls -----

echo "=== Final ls $CHAPTERS_DIR ==="
ls "$CHAPTERS_DIR"

if [[ -d "$UNRESOLVED_DIR" ]] && [[ -n "$(ls -A "$UNRESOLVED_DIR" 2>/dev/null || true)" ]]; then
    echo
    echo "=== ls $UNRESOLVED_DIR ==="
    ls "$UNRESOLVED_DIR"
fi
