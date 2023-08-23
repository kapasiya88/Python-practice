# write a function to find the first non-repeating character in a string.
from collections import Counter 
def printNonrepeated(string):
    freq = Counter(string)
    print(freq)
    for i in string:
        if(freq[i] == 1):
            print("First non-repeating character is " + i)
            break

string = "geeksforgeeks"
printNonrepeated(string)