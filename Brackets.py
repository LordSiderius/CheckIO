import string

def checkio(input):
    set_dig = set(string.digits + "+" + "-" + "*" + "/")
    for item in set_dig:
        input = input.replace(item ,"")


    while ('()' in input or '[]' in input or '{}'in input):
        print("while start:", input)
        input = input.replace('()', "")
        input = input.replace('[]', "")
        input = input.replace('{}', "")


    print("input_last", input)

    if input is '':
        return True
    else:
        return False

# print(checkio("((5+3)*2+1)")) #== True
# print(checkio("{[(3+1)+2]+}")) #== True
# print(checkio("(3+{1-1)}")) #== False
# print(checkio("[1+1]+(2*2)-{3/3}")) #== True
# print(checkio("(({[(((1)-2)+3)-3]/3}-3)")) #== False
# print(checkio("2+3")) #== True

print(checkio("({[3]})-[4/(3*{1001-1000}*3)/4]"))