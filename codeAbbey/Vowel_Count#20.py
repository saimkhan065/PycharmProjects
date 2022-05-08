test_string1 = "mslefinnuaxikcbuuu lakygt aunptkzfx eoopkctwue"
test_string2 = "v xdzkibqervgikds cnh  bdmile xwaooe w  cqjl  xnv"
test_string3 = "iixxhrcy   swosfimt  vsaxu hovm jksjgaoub vkuyuqyketraa"
test_string4 = "wvzfl rgmzdmpvvhv wu x mqw jsdgavtliyigfq okvgpawfs abj ny"

vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowel(string):
    count = 0
    for char_s in string:
        if char_s in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowel(test_string1))
    print(count_vowel(test_string2))
    print(count_vowel(test_string3))
    print(count_vowel(test_string4))
