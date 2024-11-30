# question number 149

def solve(points):
    n = len(points)
    d = {}
    for i in range(n):
        x, y = points[i][0], points[i][1]
        for j in range(i + 1, n):
            x1 = x - points[j][0]
            y1 = y - points[j][1]
            b = x1 * y - y1 * x
            d[(y1, x1, b)] = 0
    for i in range(n):
        x, y = points[i][0], points[i][1]
        for j in d:
            if j[1] * y == j[0] * x + j[2]:
                d[j] += 1
    m = 1
    for x in d:
        m = max(m, d[x])
    return m

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
res = solve(points)
print(res)
        
def solve2(p):
    
    n = len(points)
    def slope(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return (dy, dx) if dx != 0 else ('inf', 0)
    
    max_points = 0
    for i in range(n):
        slopes = {}
        duplicate = 1  # Count the current point
        for j in range(i + 1, n):
            if points[i] == points[j]:
                duplicate += 1  # Count duplicates
            else:
                s = slope(points[i], points[j])
                slopes[s] = slopes.get(s, 0) + 1
        
    max_points = max(max_points, (max(slopes.values(), default=0) + duplicate))