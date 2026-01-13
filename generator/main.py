import itertools

def get_substrings(words, min_len=2, max_len=4):
    """Generates substrings strictly between min_len and max_len."""
    subs = set()
    for word in words:
        for i in range(len(word)):
            # Ensure we don't go beyond the word length or the max_len constraint
            for j in range(i + min_len, min(i + max_len, len(word)) + 1):
                subs.add(word[i:j])
    return list(subs)

def get_leet_variations(text):
    """
    Generates variations replacing characters with look-alike numbers/letters.
    NO random numbers added.
    """
    leet_map = {
        'a': ['a', '4'],
        'e': ['e', '3'],
        'i': ['i', '1'],
        'o': ['o', '0'],
        's': ['s', '5', 'z'],
        't': ['t', '7'],
        'l': ['l', '1'],
        'u': ['u', 'v'], 
        'v': ['v', 'u']
    }
    
    # Generate all combinations of substitutions for the input text
    options = [leet_map.get(c, [c]) for c in text.lower()]
    return [''.join(p) for p in itertools.product(*options)]

def main():
    print("Generating strict 2-3-4 char usernames...")
    keywords = ["louis", "vanhove", "itutoronline", "tutor", "louv", "tele"]
    
    # 1. Get base substrings (Strictly 2 to 4 chars long)
    substrings = get_substrings(keywords, min_len=2, max_len=4)
    
    variations = set()

    # 2. Generate Leet variations for these substrings
    for sub in substrings:
        vars = get_leet_variations(sub)
        for v in vars:
            # Double check length constraint
            if 2 <= len(v) <= 4:
                variations.add(v)

    # 3. Combine short substrings (e.g. 2 char + 2 char = 4 char)
    # We only need substrings of length 2 for this, as 2+3=5 (too long)
    short_subs = [s for s in substrings if len(s) == 2]
    
    for s1 in short_subs:
        for s2 in short_subs:
            combined = s1 + s2
            # Strictly check combined length
            if len(combined) <= 4:
                # Get leet vars for the combined string
                vars = get_leet_variations(combined)
                for v in vars:
                    variations.add(v)

    # Sort and Save
    sorted_list = sorted(list(variations))
    
    filename = "strict_usernames_234.txt"
    try:
        with open(filename, "w") as f:
            f.write("\n".join(sorted_list))
        print(f"\nSUCCESS! Generated {len(sorted_list)} usernames (Lengths 2, 3, 4).")
        print(f"They have been saved to '{filename}' in this folder.")
    except Exception as e:
        print(f"\nError creating file: {e}")

if __name__ == "__main__":
    main()
    # Keeps window open
    input("\nPress Enter to exit...")