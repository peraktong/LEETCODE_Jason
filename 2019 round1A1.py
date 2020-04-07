

def dfs(R, C, can_go, cur_i, cur_j, visited, path, result):
    if len(visited) == R * C: # successfully find path
        result[:] = path
        return True
    for next_i, next_j in can_go[(cur_i, cur_j)]:
        if (next_i, next_j) not in visited and dfs(R, C, can_go, next_i, next_j, visited | {(next_i, next_j)}, path + [(next_i, next_j)], result):
            return True
    return False

def valid(i, j, ii, jj):
    return (i != ii) and (j != jj) and (i - j) != (ii - jj) and (i + j) != (ii + jj)

def is_possible(R, C):
    can_go = {}
    for i in range(R):
        for j in range(C):
            can_go[(i, j)] = {(ii, jj) for ii in range(R) for jj in range(C) if valid(i, j, ii, jj)}

    result = []
    for i in range(R):
        for j in range(C):
            if dfs(R, C, can_go, i, j, set(), [], result):
                return result
    return []
    
def main():
    T = int(input())
    for t in range(1, T+1):
        R, C = map(int, input().split())
        res = is_possible(R, C)
        if len(res) == 0:
            print("CASE #{}: IMPOSSIBLE".format(t))
        else:
            print("CASE #{}: POSSIBLE".format(t))
            for i, j in res:
                print("{} {}".format(i+1, j+1))
        
main()