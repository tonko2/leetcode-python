class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        d = []
        for asteroid in asteroids:
            d.append(asteroid)            
            while len(d) > 1:
                asteroid1 = d[-1]
                asteroid2 = d[-2]
                if (asteroid1 < 0 and asteroid2 > 0) or (asteroid1 > 0 and asteroid2 < 0):                    
                    d.pop()
                    d.pop()
                    if abs(asteroid1) == abs(asteroid2):
                        continue
                    elif abs(asteroid1) > abs(asteroid2):
                        d.append(asteroid1)
                    else:
                        d.append(asteroid2)
                else:
                    break          
        return d