import numpy

input = [1, 2,3,4,5,6]

def uni_killer(data):

    list = []
    output = []

    for number in data:
        count = 0
        for item in data:

            if number == item:
                count += 1

        list.append([number, count])

    print("original list: ", list)
    print("list 0: ", list [0][1])

    for item in range(len(list)):
        print("item in list: ", list[item])
        if list[item][1] != 1:
            output.append(list[item][0])


    print("output:", output)

    return output

uni_killer(input)