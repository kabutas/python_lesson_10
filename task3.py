def can_find(bigrams: list, words: list) -> bool:
    result = []
    singe_string = " ".join(words)
    # print(singe_string)
    for i in bigrams:
        if i in singe_string:
            result.append(True)
        else:
            result.append(False)
    if False in result:
        return False
    else:
        return True


print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
# "cu" does not exist in any of the words.
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))
