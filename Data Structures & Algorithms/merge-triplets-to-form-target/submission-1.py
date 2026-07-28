class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a1 = b1 = c1 = False

        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue

            if a==target[0]:
                a1 = a1 or True
            else:
                b1 = b1 or False

            if b==target[1]:
                b1 = b1 or True
            else:
                b1 = b1 or False
            
            if c==target[2]:
                c1 = c1 or True
            else:
                c1 = c1 or False
        

        return a1 and b1 and c1
            