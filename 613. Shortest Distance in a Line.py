"""

# Write your MySQL query statement below


SELECT MIN(ABS(p1.x-p2.x)) AS shortest
FROM point p1 JOIN point p2 ON p1.x!=p2.x;

"""

A = [1,2,3,4,3,2,1,9]
print(A[~5])
print(0^1)