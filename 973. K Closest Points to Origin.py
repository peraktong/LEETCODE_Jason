points = [[3,3],[5,-1],[-2,4]]

def s2(x):
    return x[0]**2+x[1]**2

def k_closest(points,k):

    points.sort(key=s2)
    print(points[:k])

k_closest(points=points,k=2)