def evaluace(letter, delta):

    if letter == " ":
        return letter

    shifted_letter = ord(letter) +   + delta

    if (shifted_letter) < 97:
        return chr(123 - (97 - shifted_letter))

    elif (shifted_letter) > 122:
        return chr(96 + (shifted_letter - 122))
    else:
        return chr(shifted_letter)

def to_encrypt(text, delta):

    result = ""
    for letter in text:
        result += evaluace(letter, delta)
    return result


text = "z"
delta = 1

print(to_encrypt(text, delta))