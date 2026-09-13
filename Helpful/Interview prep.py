def missing_letter(list):
    for num in range(len(list) - 1):
        if ord(list[num + 1]) - ord(list[num]) > 1:
            return chr(ord(list[num]) + 1)
        