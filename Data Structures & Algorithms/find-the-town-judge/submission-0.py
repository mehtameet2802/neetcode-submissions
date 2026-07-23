class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [[0,0] for i in range(n)]

        for u,v in trust:
            arr[u-1][1]+=1
            arr[v-1][0]+=1
        
        for j, ele in enumerate(arr):
            i = ele[0]
            o = ele[1]
            if i == n-1 and o == 0:
                return j+1

        return -1