"""
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""
def gcdOfStrings(str1, str2):
    l1,l2=len(str1),len(str2)
    def isDivisor(l):
        if l1%l or l2%l:
            return False
        f1,f2=l1//l,l2//l
        return str1[:l]*f1==str1 and str1[:l]*f2==str2

    for l in range(min(l1,l2),0,-1):
        if isDivisor(l):
            return str1[:l]
    return ""
    

str1 = "LEET"
str2 = "CODE"
res=gcdOfStrings(str1, str2)
print(res)
str1 = "ABABAB"
str2 = "ABAB"
res=gcdOfStrings(str1, str2)
print(res)
str1 = "ABCABC"
str2 = "ABC"
res=gcdOfStrings(str1, str2)
print(res)

"""Time complexity:O(min(m,n)).O(n+m) 
Approach: consider min length of both strings
run a loop over that length ex from 4 to 1,
check for each length if it's a divisor 
seperate method for checking
for length l, divide it with strings length if it's !=0, return false
else find new factors by using len(str1)//l and len(str2)//l
return true only if factor*str1[:l]==str1 and factor2*str1[:l]==str2"""