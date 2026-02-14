def match_words(words):
    ctrl = 0
    lst = []
    for word in words:
        if len(words) > 1 and word[0] == word[-1]:
            ctrl = ctrl+1
            lst.append(word)
    print("List of words with first and lastn character same\n", lst)
    return ctrl
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and lastcharacter same:", count)