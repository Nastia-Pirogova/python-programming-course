def count_letters():
    text = input("Введіть текст: ").lower()
    print("Текст:", text)

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowel_count = 0
    consonant_count = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Кількість голосних:", vowel_count)
    print("Кількість приголосних:", consonant_count)

    if vowel_count > consonant_count:
        print("У тексті більше голосних літер.")
    elif consonant_count > vowel_count:
        print("У тексті більше приголосних літер.")
    else:
        print("Кількість голосних і приголосних однакова.")

    return vowel_count, consonant_count


count_letters()
