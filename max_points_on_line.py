from  collections import defaultdict
def maxPoints(points):
    res = 1
    for i in range(len(points)):
        p1 = points[i]
        count = defaultdict(int)
        for k in range(i+1,len(points)):
            p2 = points[k]
            if p2[0] == p1[0]:
                slope = float("inf")
            else:
                slope = (p2[1]-p1[1])/(p2[0]-p1[0])
            count[slope] += 1
            res = max(res,count[slope]+1)
    return res

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points2 = [[1,1],[2,2],[3,3]]
print(maxPoints(points))
print(maxPoints(points2))