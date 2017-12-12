from data import DICTIONARY, LETTER_SCORES

print(LETTER_SCORES)
print('\n')

words = []

with open(DICTIONARY) as dict_file:
    for line in dict_file.readlines():

        words.append(line.strip('\n'))
