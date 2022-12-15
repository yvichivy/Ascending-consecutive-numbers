def ascending(s: str) -> bool:
    # Split the string into substrings of consecutive numbers
    substrings = [s[i] for i in range(len(s)) if i == 0 or s[i-1].isnumeric() != s[i].isnumeric()]

    # Return True if any substring consists of ascending numbers, False otherwise
    return any(int(substring[0]) < int(substring[-1]) for substring in substrings if substring.isnumeric())
