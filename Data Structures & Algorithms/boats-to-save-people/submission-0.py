class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people)

        p1 = 0
        p2 = len(people) - 1

        cnt = 0

        while p1<=p2:
            if (people[p1] + people[p2]) <= limit:
                p1+=1
                p2-=1
            elif people[p2] <= limit:
                p2-=1
            else:
                p1+=1
            
            cnt+=1
        
        return cnt