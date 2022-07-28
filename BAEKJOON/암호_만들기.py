from itertools import combinations


if __name__ == "__main__":
    all_vowels = {"a", "e", "i", "o", "u"}

    consonants = set()
    vowels = set()
    all_chars = set()

    L, C = map(int, input().split())
    chars = list(input().split())
    for char in chars:
        if char in all_vowels:
            vowels.add(char)
        else:
            consonants.add(char)

    all_chars = consonants | vowels

    consonant_list = list(combinations(consonants, 2))
    vowel_list = list(vowels)


    answers = set()

    left_num = L - 3

    for v in vowel_list:
        all_chars.remove(v)
        for c1, c2 in consonant_list:
            all_chars.remove(c1)
            all_chars.remove(c2)
            for case in combinations(all_chars, left_num):
                left_case = list(case)
                left_case.extend([v, c1, c2])
                left_case.sort()
                answers.add("".join(left_case))
            all_chars.add(c1)
            all_chars.add(c2)
        all_chars.add(v)
    answers = list(answers)
    answers.sort()
    for a in answers:
        print(a)



