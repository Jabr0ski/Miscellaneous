#prints numbers up to i using for loop
def fl():
    l = []
    for i in range(0, 5):
        l.append(i)
    print(l)

#asks for user input and concatenates strings to greet
def cc():
    name = input("what's ur name? ")
    s1 = "Hello "
    s2 = name
    s3 = s1+s2
    print(s3)

#prints odd numbers up to i using while loop
def wl():
    l = []
    i = 0
    while i < 5:
        if (i%2)==1:
            l.append(i)
        i += 1
    print(l)

wl()