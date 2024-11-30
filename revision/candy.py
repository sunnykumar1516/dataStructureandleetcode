def solve(ratings):
    candies = [1 for i in range(len(ratings))]
    candies2 = [1 for i in range(len(ratings))]
    for i in range(1,len(candies)):
        print(i)
        if ratings[i]> ratings[i-1]:
            candies[i]= candies[i-1]+1
    print(candies)
    for i in range(len(ratings)-2,-1,-1):
        if ratings[i]> ratings[i+1]:
            candies2[i]= candies[i+1]+1
    print(candies2)
    res = [ max(candies[i],candies2[i]) for i in range(len(candies))]
    print(res)

ratings = [1,0,2]
solve(ratings)