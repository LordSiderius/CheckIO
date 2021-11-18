input = []

def all_the_same(input):
    result = True
    for item in input:
        for element in input:
            if item != element:
                result = False

    return result

print(all_the_same(input))