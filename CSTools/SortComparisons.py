import random
import time
import collections

def insertSort(l):
    for j in range(len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] > key:
            l[i + 1] = l[i]
            i = i - 1
            l[i + 1] = key
    return l

def mergeSort(l):
    if len(l) >1: 
        mid = len(l) // 2 #Finding the mid of the array 
        L = l[:mid] # Dividing the array elements  
        R = l[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                l[k] = L[i] 
                i+=1
            else: 
                l[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            l[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            l[k] = R[j] 
            j+=1
            k+=1
    return l

# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ int((index)%10) ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(l): 
  
    # Find the maximum number to know number of digits 
    max1 = max(l) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(l,exp) 
        exp *= 10

    return l

def randomList(a, m):
    #r = random.randint(0, a)
    intlist = []
    for i in range(a):
        intlist.append(random.randint(1, m))
    for i in range(len(intlist)):
        s = random.randint(1, a-1)
        intlist[i], intlist[s] = intlist[s], intlist[i]
    return intlist
    
def ascTest(nl):
    asc = True
    for i in range(len(nl)-1):
        if nl[i+1] < nl[i]:
            print("Error: Not ascending order.")
            asc = False
            break
    if asc == True:
        print("Correct: Ascending order.")
        
def parTest(l, nl):
    if collections.Counter(l) == collections.Counter(nl): 
        print ("Correct: The sorted list contains all the same elements as the unsorted list.") 
    else : 
        print ("Error: The sorted list does not contain all the same elements as the unsorted list.") 

def main():
    a = input("How many elements in list? ")
    m = input("What is the max value number in the list? ")
    l = randomList(int(a), int(m))
    print("This is the randomised list:\n" + str(l))
    a = input("IS (Insert Sort), MS (Merge Sort), or RS (Radix Sort)?")
    a = a.strip()
    a = a.upper()
    if a == "IS" or a == "I":
        stime = time.time()
        nl = insertSort(l)
        istime = time.time () - stime
        print("This is the insertSorted list:\n" + str(nl))
        
    if a == "MS" or a == "M":
        stime = time.time()
        nl = mergeSort(l)
        istime = time.time () - stime
        print("This is the mergeSorted list:\n" + str(nl))
        
    if a == "RS" or a == "R":
        stime = time.time()
        nl = radixSort(l)
        istime = time.time () - stime
        print("This is the radixSorted list:\n" + str(nl))

    print("It took " + str(istime) + " to compute.")
    ascTest(nl)
    parTest(l, nl)


main()
    