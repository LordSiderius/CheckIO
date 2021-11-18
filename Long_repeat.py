def long_repeat(text):
    buffer = text[0]
    counter = 0
    max_count = 0
    for letter in text:
        if buffer == letter:
            counter += 1
            max_count = counter
        else:
            buffer = letter
            # max_count = counter
            counter = 1

    return max_count

print(long_repeat('sdsffffse'))
print(long_repeat('ddvvrwwwrggg'))