import random

#simulates the roulette for the 
#param f = number of spins
#param c = selected colour
def roulette(f,c):
    count = 0
    highestLossStreak = 0
    resList = []
    for x in range (0, f):
        Result = []
        Roll = ""
        vars = ["R","B"]
        while c != Roll:
            Roll = (random.choice(vars))
            Result.append(Roll)
        if len(Result) > highestLossStreak:
            highestLossStreak = len(Result)
        print (Result)
        count += len(Result)
        resList.append(Result)
    resListCalc(resList)
    print ("Average of", count/f, "spins before winning.\n")
    print ("The highest amount of bets until winning was", highestLossStreak,".\n")
    main()

#calculates percentage of wins corresponding to number of spins
#param rl = list of lists of sequence of results until winning colour is spun
def resListCalc(rl):
    #lists length of lists in rl list, the len representing 
    #number of spins until the winning colour is spun
    lengthList = [len(x) for x in rl]
    print(lengthList)
    for x in range(1, max(lengthList) + 1):
        occurRate = (lengthList.count(x)/len(lengthList)) * 100
        print(occurRate, "% of wins on spin number", x, "\n")
        

def main():
    c = ""
    f = int(input("Input the number of wins to simulate until. "))
    while c != "R" and c !="B":
        c = input("Input the bet colour, R or B. ")
        c = c.upper()
    roulette(f,c)
    
print ("This program intends to display statistics relating to" \
       "\nThe Martingale strategy of roulette betting. This is" \
       "\nwhere you bet on one colour, red or black, doubling your" \
       "\nbet size after each loss to cover your debt until your" \
       "\ncolour eventually wins and you earn your original bet" \
       "\nback in profit.\n")

main()