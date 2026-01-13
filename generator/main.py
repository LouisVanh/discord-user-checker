import itertools

def get_substrings(words, min_len=2, max_len=5):
    subs = set()
    for word in words:
        # Get standard substrings
        for i in range(len(word)):
            for j in range(i + min_len, min(i + max_len, len(word)) + 1):
                subs.add(word[i:j])
    return list(subs)

def get_leet_variations(text):
    # Only replace vowels/similar shapes, no random numbers
    leet_map = {
        'a': ['a', '4'],
        'e': ['e', '3'],
        'i': ['i', '1'],
        'o': ['o', '0'],
        's': ['s', '5', 'z'],
        't': ['t', '7'],
        'l': ['l', '1'],
        'u': ['u', 'v'], 
        'v': ['v', 'u'] # v can look like u
    }
    
    # Generate all combinations of substitutions
    options = [leet_map.get(c, [c]) for c in text.lower()]
    return [''.join(p) for p in itertools.product(*options)]

def main():
    print("Generating usernames, please wait...")
    keywords = ["louis", "vanhove", "itutoronline", "tutor", "louv", "tele"]
    
    # 1. Get base substrings (2-5 chars)
    substrings = get_substrings(keywords, 2, 5)
    
    variations = set()

    # 2. Generate Leet variations for simple substrings
    for sub in substrings:
        vars = get_leet_variations(sub)
        for v in vars:
            if 2 <= len(v) <= 5:
                variations.add(v)

    # 3. Combine short substrings to maximize count (e.g. 'lo' + 'tu' = 'lotu')
    # Filter for very short bases to combine
    short_subs = [s for s in substrings if len(s) <= 3]
    
    # Create combinations (Base + Base)
    for s1 in short_subs:
        for s2 in short_subs:
            combined = s1 + s2
            if 2 <= len(combined) <= 5:
                # Get leet vars for the combined string
                vars = get_leet_variations(combined)
                for v in vars:
                    variations.add(v)

    # Sort and Save
    sorted_list = sorted(list(variations))
    
    filename = "strict_usernames.txt"
    try:
        with open(filename, "w") as f:
            f.write("\n".join(sorted_list))
        print(f"\nSUCCESS! Generated {len(sorted_list)} usernames.")
        print(f"They have been saved to a file named '{filename}' in this same folder.")
    except Exception as e:
        print(f"\nError creating file: {e}")

if __name__ == "__main__":
    main()
    # This line keeps the window open:
    input("\nPress Enter to exit...")