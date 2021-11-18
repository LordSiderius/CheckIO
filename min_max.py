input = [["sracka"]]

def loupac(data):
    if type(data) is list | tuple:
        for item in data:
            list.append(loupac(list, item))
            print("item:", item)

    return

def min(*args, **kwargs):
    new_args = loupac(args)
    print("args: ", new_args)
    key = kwargs.get("key", None)

    if key is None:
        minimum = new_args[0]
        for element in new_args:
            if element < minimum:
                minimum = element

    else:
        new_args = []
        for element in args:
            new_args.appenmd(key(element))

        minimum = new_args[0]
        for element in args:
            if element < minimum:
                minimum = element

    return minimum



# print("zasrany minimum: ", min(1, 2, 3, 4, 0))
print("loupac: ", loupac(list, [[[1, 2, 3, 4, 0]]]))

