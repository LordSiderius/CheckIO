data = [1,2,3]


def checkio(data):
    try:
        return_sum = data.pop(0) + sum(data)
    except:
        return 0
    return return_sum

# print("data pop: ", data.pop(0))
print(checkio([1,2,3]))