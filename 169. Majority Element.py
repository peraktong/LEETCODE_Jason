import collections
array = [2,2,1,1,1,2,2]

counts = collections.Counter(array)
print(max(counts.keys(),key=counts.get))
array.sort()
print(array[len(array)//2])