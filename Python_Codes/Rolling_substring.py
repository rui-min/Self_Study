"""
@completion: July 1, 2021
@author: Rui Min
@topic: find all permutations of a given shorter string within a longer string
"""
# The idea comes from Rabin-Karp Substring Search but this algorithm deals with 
# unordered situation. That is, find all permutations of the shorter string "s" within
# the longer one "b". Time efficiency is O(b-s). Done with "unordered Rolling Hash Function"

import string
def hashGenerate(charCode, SCALE):
    value = 1
    for c in string.ascii_lowercase:
        charCode[c] = value
        value += 1
    for c in string.ascii_uppercase:
        charCode[c] = value
        value += 1
    for key in charCode:
        charCode[key] **= SCALE
    
def per(s,b):
    charCode = {}
    SCALE = 4
    hashGenerate(charCode, SCALE)
    print(charCode)     # testing purpose
    # first part below building rolling hash values and building position list
    sHash = 0
    for char in s:
        sHash += charCode[char]
    currentHash = 0
    for i in range(len(s)):
        currentHash += charCode[b[i]]   # initialize as first len(s) sum of code(b[i])
    answerIndex = []
    for i in range(len(b) - len(s)+1):
        if (i==0) and (currentHash==sHash):
            answerIndex.append(i)
        else:
            # unordered rolling hash function below:
            currentHash = currentHash -charCode[b[i-1]] + charCode[b[i+len(s)-1]]
            if currentHash == sHash:
                answerIndex.append(i)
    
    print(answerIndex)  # first part ends here with positions list
# ======================================================================================
    # second part check whether each position's substring is really suitable
    sDict = {}
    for i in range(len(s)):
        sDict[s[i]] = sDict.get(s[i],0) +1
    count = 0
    for pos in answerIndex:
        sub_b = b[pos:(pos+len(s))]
        subDict ={}
        for i in range(len(sub_b)):
            subDict[sub_b[i]] = subDict.get(sub_b[i],0) + 1     # counting idiom
        flag = True
        for i in range(len(sub_b)):
            if sDict.get(sub_b[i]) != subDict.get(sub_b[i]):    # .get() to avoid key error
                flag = False
                break
        if flag:
            count += 1
            print(pos, sub_b)

    return count

if __name__ == "__main__":
    s = "abbc"
    b = "cbabadcbbabbcbabaabccbabc"
    print(per(s,b))
    s = "abbc"
    b = "bcda"
    print(per(s,b))