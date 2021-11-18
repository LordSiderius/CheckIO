import string
import random

def id_generator(size= random.randrange(15), chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def password_checker(password):
    pass_len = False

    try:
        passw = str(password)
    except:
        print("not only a string")
        return

    print(len(passw))
    if len(passw) >= 10:
        pass_len = True



    s0 = set()
    s1 = set(passw)
    s2 = set(string.ascii_lowercase)
    s3 = set(string.digits)
    s4 = set(string.ascii_uppercase)

    pass_low = s1.intersection(s2) != s0
    pass_dig = s1.intersection(s3) != s0
    pass_upp = s1.intersection(s4) != s0

    print("len: ", pass_len)
    print("lower: ", s1.intersection(s2) != s0)
    print("digits: ", s1.intersection(s3) != s0)
    print("upper: ", s1.intersection(s4) != s0)

    return pass_len and pass_low and pass_dig and pass_upp

#-----------------------------------------------------------------------------------------------------

password = id_generator()

print(password)

print("Result: ", password_checker(password))