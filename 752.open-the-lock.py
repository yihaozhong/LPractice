

#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from queue import Queue
class Solution:
    def plusOne(self,input : str, idx: int):
        if input[idx] == '9':
            input = input[:idx] + '0' + input[idx+1:]
        else:
            input = input[:idx] + str(int(input[idx])+1) + input[idx+1:]
        return input

    def minusOne(self, input, idx):
        if input[idx] == '0':
            input = input[:idx] + '9' + input[idx+1:]
        else:
            input = input[:idx] + str(int(input[idx])-1) + input[idx+1:]
        return input

    def openLock(self, deadends: List[str], target: str) -> int:
        # put deadends and visited together in a hash set
        visited = set()
        dead = set()
        for i in deadends:
            dead.add(i)
        
        # create a queue for BFS
        q = Queue()

        # BFS
        step = 0
        q.put("0000")
        visited.add("0000")

        while q.empty() == False:
            sz = q.qsize()

            # for every direction if a node from queue

            for i in range(sz):
                cur = q.get()
                if (cur in dead):
                    continue
                if (cur == target):
                    return step

                # for every adj node
                for j in range(4):
                    up = self.plusOne(cur, j)
                    down = self.minusOne(cur, j)
                    if (up not in visited):
                        q.put(up)
                        visited.add(up)
                    if (down not in visited):
                        q.put(down)
                        visited.add(down)


            step += 1

        return -1

    #O(N^2∗A^N+D) where A is the number of digits in our alphabet, N is the number of digits in the lock, and D is the size of deadends
#print(Solution.openLock(Solution(),["0201","0101","0102","1212","2002"], "0202"))
 
# @lc code=end

