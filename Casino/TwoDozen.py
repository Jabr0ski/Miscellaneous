import random

def twoDozen(c,d,p,f):
    result = 0
    final = 0
    win = 0
    loss = 0
    winList = []
    if c == "1" or d == "1":
        winList.extend(range(1, 13))
    if c == "2" or d == "2":
        winList.extend(range(13, 25))
    if c == "3" or d == "3":
        winList.extend(range(25, 37))
    for x in range (0, f):
        # 0 to 37 to account for 0 and 00 spins
        result = random.randint(0, 37)
        if result in winList:
            final += p/2
            win += 1
        else:
            final -= p
            loss += 1
    print("\nYou come out with $", final, "with", win,"win/s and", loss,"loss/es.")

def main():
    valid = 0
    c = ""
    d = ""
    p = int(input("Input the full principal bet to be split. "))
    f = int(input("Input the number of roulette spins to simulate. "))
    while c != "1" and c !="2" and c !="3":
        c = input("Input the first of the two dozens to bet on, 1, 2 or 3. ")
    while (d != "1" and d !="2" and d !="3") or d == c:
        d = input("Input the second of the two dozens to bet on, 1, 2 or 3. ")
    twoDozen(c,d,p,f)
    
print ("This program intends to display statistics relating to" \
       "\nThe Martingale strategy of roulette betting. This is" \
       "\nwhere you bet on one colour, red or black, doubling your" \
       "\nbet size after each loss to cover your debt until your" \
       "\ncolour eventually wins and you earn your original bet" \
       "\nback in profit.\n")

main()