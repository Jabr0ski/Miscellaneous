import re
import pyttsx3
KiwiAcc = pyttsx3.init()

print(KiwiAcc.getProperty('voices'))
def kiwifi(f):
    sub_dict = {'a':'e','e':'i','i':'u','o':'u','u':'a'}
    regex = '|'.join(sub_dict)
    return re.sub(regex, lambda m: sub_dict[m.group()], f)
    
def main():
    f = input("Type out a word or sentence you want Kiwified. \n")
    newKiwi = kiwifi(f)
    print(newKiwi + "\n")
    KiwiAcc.say(newKiwi)
    KiwiAcc.runAndWait()
    main()

main()