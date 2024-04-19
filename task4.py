list_of_vowels = {'a', 'e', 'i', 'o', 'u'}


#                      without lambda
def starts_with_vowel(words: list[str]) -> list[str]:
    vovel_strings_list = []
    for i in words:
        if i[0].lower() in list_of_vowels:
            vovel_strings_list.append(i)
    return vovel_strings_list


print(starts_with_vowel(['bananna', 'apple', 'cat', 'dog', 'wall', 'Air', 'orange', 'elephant']))
