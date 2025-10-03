def middle_chars(word: str) -> str:
    n = len(word)
    mid = n // 2
    return word[mid] if n % 2 else word[mid - 1: mid + 1]

print(middle_chars('test'))
print(middle_chars('testing'))