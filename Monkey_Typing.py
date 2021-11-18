string = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."
key = {"sum", "hamlet", "infinity", "anything"}

def metoda(data, item):
    present = False
    if item in data:
        present = True

    return present


def word_expolorer(data, key):
    data = data.lower()
    count = 0
    for item in key:
        print("item:", item)
        metoda(data, item)
        if metoda(data, item) is True:
            count += 1

        print("count: ", count)

    # print("key: ",list)
    return count

print("vysledek: ", word_expolorer(string, key))