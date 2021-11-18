import random, string

# def id_generator(size= random.randrange(10^5), chars=string.ascii_uppercase + " " +string.ascii_lowercase + "!!!!!!!"):
#     return ''.join(random.choice(chars) for _ in range(size))

def most_wanted_letter(word):
    d = dict()
    list = []
    word = word.lower()

    # creates dictionary from input string
    for letter in word:
        if set(letter).intersection(set(string.ascii_lowercase)):
            print("letter:", letter)
            # look for letters one by one and adding new ones to dictionary
            d.setdefault(letter, 0)
            # add value +1 for every presented letter
            d[letter] += 1

        print("dictionary: ", d)

    # look for maximum value and save it
    inverse = [(value, key) for key, value in d.items()]
    maximum = max(inverse)[0]

    print("maximum: ", maximum)

    # save keys from maximum value, my keys are letters
    for key, value in d.items():
        if value == maximum:
            # add letters(keys) with maximum value to list
            list.append(key)

    # sort the list by alphabet
    list.sort()

    print("list:", list)
    # write the most wanted letter :D
    print("first in alphabet:", list[0])

    return list[0]


# word = id_generator()

word = "fdsoh  ihjafpasi  )(  asdwaede"
print("slovo:", word)

print(most_wanted_letter(word))