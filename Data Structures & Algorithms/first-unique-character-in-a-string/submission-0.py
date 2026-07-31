class Solution:
    def firstUniqChar(self, s: str) -> int:

        '''
        Pattern - Frequency Count

        TC - O(n)
        SC - O(1)
        '''

        arr = [0]*26

        for i,ch in enumerate(s):
            ind = ord(ch)-ord('a')            
            arr[ind]+=1
        
        for i,ch in enumerate(s):
            ind = ord(ch)-ord('a')
            if arr[ind]==1:
                return i
        
        return -1