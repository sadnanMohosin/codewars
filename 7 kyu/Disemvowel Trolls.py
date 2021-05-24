def disemvowel(string):
    no_vowel = []
    for i in string:
        if i not in "aeiouAEIOU":
            no_vowel.append(i)
    return "".join(no_vowel)
