# question number 502
import heapq as hp

def solve(k, w, profits, capital):
    work = []
    buffer = []
    for i in range(len(profits)):
        sample = (capital[i],profits[i])
        hp.heappush(work,sample)
    print(work)
    capital.sort()
    
    for i in range(k):
        while work and work[0][0] <= w:
            c,p = hp.heappop(work)
            hp.heappush(buffer,(-p,c))
        if len(buffer) == 0:
            return w
        p,c = hp.heappop(buffer)
        
        w = w+ (p*-1)
    return w
        
        
        
            
            
        
    
    
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

k = 1
w = 0
profits = [1,2,3]
capital = [1,1,2]
print(solve(k,w,profits, capital))