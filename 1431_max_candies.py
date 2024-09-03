'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.'''

def kidsWithCandies(candies, extraCandies):
    max_candies=max(candies)
    res=[]
    for i in candies:
        if i+extraCandies >=max_candies:
            res.append(True)
        else:
            res.append(False)
    # result=[False]*len(candies)
    # max_candies=max(candies)
    # for i in range(len(candies)):
    #     if candies[i]+extraCandies>=max_candies:
    #         result[i]=True
    print(result)



candies = [2,3,5,1,3]
extraCandies = 3
kidsWithCandies(candies, extraCandies)
candies = [4,2,1,1,2]
extraCandies = 1
kidsWithCandies(candies, extraCandies)
candies = [12,1,12]
extraCandies = 10
kidsWithCandies(candies, extraCandies)

'''Time complexity:
The time complexity of the algorithm is O(n) since we iterate through the candies array twice.

Space complexity:
The space complexity of the algorithm is O(n) since we store the result in a list of length n.
'''