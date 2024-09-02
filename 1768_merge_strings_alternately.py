"""
Problem statement
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""
def mergeAlternately(word1, word2):
    # final_string=""
    # count=0
    # word_len1=len(word1)
    # word_len2=len(word2)
    # greatest_len=max([word_len1,word_len2])
    # while count!=greatest_len:
    #     if count<len(word1):
    #         final_string+=word1[count]
    #     if count<len(word2):
    #         final_string+=word2[count]
    #     count+=1    
    res=[]
    i,j=0,0
    while i<len(word1) and j<len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i+=1
        j+=1
    res.append(word1[i:])
    res.append(word2[j:])
    final_string="".join(res)
    print(final_string)
    
        


word1= "abcd"
word2= "pq"
mergeAlternately(word1,word2)
word1= "ab"
word2= "pq"
mergeAlternately(word1,word2)
word1= "ab"
word2= "pqrs"
mergeAlternately(word1,word2)


"""
Time Complexity: O(max(len(word1), len(word2))), where n is the length of the longer string.

Space Complexity: O(len(word1) + len(word2)), where n is the length of the merged string.
"""        