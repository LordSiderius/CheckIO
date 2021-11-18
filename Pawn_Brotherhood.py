def safe_pawns(position):
    counter = 0
    for item in position:
        safe_A = chr(ord(item[0]) - 1) + str(int(item[1]) - 1)
        safe_B = chr(ord(item[0]) + 1) + str(int(item[1]) - 1)

        match = 0
        for saves in position:
            if safe_A == saves or safe_B == saves:
                match = 1

        counter += match

    return counter

assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})  == 6
assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})  == 1