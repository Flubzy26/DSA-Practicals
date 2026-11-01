def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    if m == 0:
        print("Empty pattern! Matches at all positions.")
        return list(range(n + 1))

    if m > n:
        return []  # pattern can't be longer than text

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)

    return positions


def main():
    print("=== Naive String Matching Algorithm ===")
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")

    result = naive_string_match(text, pattern)

    if result:
        print(f"\n✅ Pattern found at indices: {result}")
        for idx in result:
            print(f"  - text[{idx}:{idx+len(pattern)}] = '{text[idx:idx+len(pattern)]}'")
    else:
        print("\n❌ Pattern not found in the text.")


if __name__ == "__main__":
    main()
