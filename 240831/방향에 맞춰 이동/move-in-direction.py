x, y = 0, 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

w = {'W': 2, 'S': 0, 'N': 1, 'E': 3}

for _ in range(int(input())):
    l, d = input().split()
    d = int(d)
    
    x, y = x + dx[w[l]] * d, y + dy[w[l]] * d
    
print(x, y)