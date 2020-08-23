import random

def roulette(f,c):
    count = 0
    maxResult = 0
    resList = []
    for x in range (0, f):
        R = "R"
        B = "B"
        Result = []
        Roll = [""]
        vars = [R,B]
        while c != Roll[0]:
            Roll = (random.sample(vars, 1))
            Result.append(Roll[0])
        if len(Result) > maxResult:
            maxResult = len(Result)
        print (Result)
        count += len(Result)
        resList.append(Result)
    print ("\nAverage of", count/f, "spins before winning.")
    print ("The highest amount of bets until winning was", maxResult,".\n")
    resListCalc(resList)
    main()

def resListCalc(rl):
    lengthList = [len(x) for x in rl]
    for x in range(1, max(lengthList) + 1):
        occurRate = (lengthList.count(x)/len(lengthList)) * 100
        print(occurRate, "% of wins on spin number", x, "\n")
        

def main():
    c = ""
    f = int(input("Input the number of roulette spins to simulate. "))
    while c != "R" and c !="B":
        c = input("Input the bet colour, R or B. ")
    roulette(f,c)
    
print ("This program intends to display statistics relating to" \
       "\nThe Martingale strategy of roulette betting. This is" \
       "\nwhere you bet on one colour, red or black, doubling your" \
       "\nbet size after each loss to cover your debt until your" \
       "\ncolour eventually wins and you earn your original bet" \
       "\nback in profit.\n")

main()