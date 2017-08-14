#!/bin/python3

import sys, string

#takes in a list s and an integer k, returns the lexicographically largest subsequence of s where each letter occurs at least k times
def solve(s, k):
    sortedstring = ''.join(sorted(s))
    numunique = sum(1 for c in string.ascii_lowercase if s.count(c) == 1)
    sub = ''
    if k != 1:
        for i in range(0, numunique):
            letter = sortedstring[i]
            if sortedstring.count(letter) < k:
                s = s.replace(letter, "1")
                sortedstring = sortedstring.replace(letter, "")
        while len(sortedstring) > 0:
            letter = sortedstring[-1]
            count = s.count(letter)
            if count >= k:
                sub += letter * count
                lastindex = s.rfind(letter)
                s = s[lastindex:]
            s = s.replace(letter, "1")
            sortedstring = sortedstring.replace(letter, "")
        return sub
            
    else:
        letter = sortedstring[-1]
        sub = letter * sortedstring.count(letter)
        lastindex = s.rfind(letter)
        for i in range(0, sortedstring.count(letter)):
            sortedstring = sortedstring.replace(letter, "", 1)
            s = s.replace(letter, "1", 1)
        while sortedstring != [] and lastindex != len(s)-1:
            letter = sortedstring[-1]
            if s.find(letter) > lastindex:
                sub += letter
                lastindex = s.find(letter)
            s = s.replace(letter, "1", 1)
            sortedstring = sortedstring.replace(letter, "", 1)
        return sub
    
 

    

if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    result = solve(s, k)
    print(result)
