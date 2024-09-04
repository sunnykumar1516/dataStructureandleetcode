import heapq as hp
class KthLargest(object):
    scores = []
    k = None

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.scores = nums
        hp.heapify(self.scores)
        self.check(k)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        hp.heappush(self.scores,val)
        print("---")
        self.check(self.k)
        return self.scores[0]

    def check(self,k):
        while len(self.scores) > self.k:
            print("current length:-",len(self.scores))
            hp.heappop(self.scores)

res = [None]
input = [[3, [4, 5, 8, 2,6,9,0]], [3], [5], [10], [9], [4]]

obj = KthLargest( input[0][0],input[0][1])

for i in range(1,len(input)):
    x = obj.add(input[i][0])
    res.append(x)

print(res)

#["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]