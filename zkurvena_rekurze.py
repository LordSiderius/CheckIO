# vraces minima z listu
def min(input):
    min = input[0]
    for item in input:
        if item < min:
            min = item

    return min


def max(input):
    max = input[0]
    for item in input:
        if item < max:
            max = item

    return max

def aaa(args, **kwargs):

    try:
        iter(args[0])
    except:
        return min(args)

    for elements in args:
        g.append(aaa(elements))

def bbb(*args):
    return args




# max(3, 2) == 3
# min(3, 2) == 2
# max([1, 2, 0, 3, 4]) == 4
# min("hello") == "e"
# max(2.2, 5.6, 5.9, key=int) == 5.6
# min([[1 ,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

ahoj = aaa(bbb([1 ,2], [3, 4], [9, 0]))
print("ahoj: ", ahoj)