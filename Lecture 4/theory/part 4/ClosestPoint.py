import math
import copy
 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)) 
  

def bruteForce(P, n):
    min_val = float('inf') 
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
  
    return min_val
  
def stripClosest(strip, size, d):
      
    min_val = d 
  
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
  
    return min_val 
  
def closestUtil(P, Q, n):
      
    if n <= 3: 
        return bruteForce(P, n) 
  
    mid = n // 2
    midPoint = P[mid]
  
    dl = closestUtil(P[:mid], Q, mid)
    dr = closestUtil(P[mid:], Q, n - mid) 
  
    d = min(dl, dr)
  
    strip = [] 
    for i in range(n): 
        if abs(Q[i].x - midPoint.x) < d: 
            strip.append(Q[i])

    return min(d, stripClosest(strip, len(strip), d))
  
def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)    
  
    return closestUtil(P, Q, n)

P = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
n = len(P) 
print("The smallest distance is", round(closest(P, n), 4))
