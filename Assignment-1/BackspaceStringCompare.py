'''
Intuition:
- two pointers starting at the end of each string
- check if characters at pointers are '#'
    - if so, decrement pointer until not equal to '#' anymore
        - while decrementing pointer, increment counter to know how many characters to skip
        - move pointer 'counter' times
- check if char at pointer are equal, if not return false
Technique: Two arrays/strings two-pointer
TC: O(n) where n is length of max(len(str1,str2))
SC: O(1)
'''
def BackspaceStringCompare(str1,str2):
    p1, p2 = len(str1)-1, len(str2)-1
    while p1 >= 0 and p2 >= 0:
        backspaceCount = 0
        while str1[p1] == '#':
            p1-=1
            backspaceCount+=1
        p1 -= backspaceCount
        backspaceCount = 0
        while str2[p2] == '#':
            p2-=1
            backspaceCount+=1
        p2 -=backspaceCount
        if str1[p1] != str2[p2]:
            return False
        p1-=1
        p2-=1
    
    #for the case that one string is longer than the other
    if p1 > 0:
        backspaceCount = 0
        while str1[p1] == '#':
            p1-=1
            backspaceCount+=1
        p1 -= backspaceCount
        print(p1)
        if p1 > 0:
            return False
    elif p2 > 0:
        backspaceCount = 0
        while str2[p2] == '#':
            p2-=1
            backspaceCount+=1
        p2 -= backspaceCount
        print(p2)
        if p2 > 0:
            return False
    return True
def main():
    print(BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep") == True)
    print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###") == False)
main()
'''
Time spent: 50 mins
'''
    