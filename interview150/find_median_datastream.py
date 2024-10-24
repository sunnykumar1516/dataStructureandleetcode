# question number 295
import heapq as hp
class MedianFinder(object):
    rightHeap = []
    leftHeap = []
   
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.leftHeap) == 0:
            hp.heappush(self.leftHeap, num*-1)
        elif len(self.rightHeap) == 0:
            hp.heappush(self.rightHeap,num)
        
        
        elif len(self.leftHeap)> 0 and len(self.rightHeap)>0:
            if num > self.leftHeap[0]*-1:
                hp.heappush(self.rightHeap,num)
            else: hp.heappush(self.leftHeap,num*-1)
            
            #balancing
            if len(self.rightHeap)>len(self.leftHeap):
                k = hp.heappop(self.rightHeap)
                hp.heappush(self.leftHeap,k*-1)
            if len(self.leftHeap)- len(self.rightHeap)>1:
                k = hp.heappop(self.leftHeap)
                hp.heappush(self.rightHeap,k*-1)
 
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
            # If even, return the average of the tops of both heaps
        return (-self.leftHeap[0] + self.rightHeap[0]) / 2.0
        
md = MedianFinder()
md.addNum(2)
md.addNum(5)
md.addNum(6)
md.addNum(3)
md.addNum(1)
md.addNum(10)
print(md.leftHeap,"-",md.rightHeap)
print(md.findMedian())