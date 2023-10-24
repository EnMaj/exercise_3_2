def count_letters(text):
    vowel = 0
    consonant = 0
    for i in range(len(text)):
        if text[i] in "йцкнгшщзхъфвпрлджчсмтьб":
            consonant += 1
        elif text[i] in "уеыаоэяию":
            vowel += 1
    print(consonant, vowel)

text = input()
count_letters(text)