"""

You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

Inputs:
M N
Matrix

Examples:
Input:
3 3
0 1 0
0 0 0
0 1 1
Output: 2

Input:
3 4
0 0 0 1
0 0 1 0
0 1 0 0
Output:

"""
import numpy as np

t = np.array([[0,1,0], [0,0,0], [0,1,1]])
k = np.array([[0,0,0,1], [0,0,1,0], [ 0,1,0,0]])
p = np.array([[0,0,0,1], [0,0,1,1], [0,1,0,1]])

# print(f'{t} :2 islands\n')
# print(f'{k} :3 islands\n')
# print(f'{p} :2 islands\n')

m = np.random.randint(2, size=(6, 5)) #random map
# print(f' {m} how many islands ? ')

def islands(map):  # input is matrix MxN that represents map
    row, columns = map.shape
    counter = 0
    visit = np.zeros((row, columns))  # array that hold information about visited cell - graph search

    def graph(i, j):
        if i < 0 or i >= row or j < 0 or j >= columns or visit[i][j] or map[i][j] == 0:
            return  # do nothing - boundries aor already visited or '0' on the map - (ocean)
        else:
            visit[i][
                j] = 1  # if cell was not visited before - put the flag '1' - (True) and check recurence graph around this cell
            graph(i + 1, j)
            graph(i - 1, j)
            graph(i, j + 1)
            graph(i, j - 1)

    for i in range(row):  # look for '1' on the map
        for j in range(columns):
            if not visit[i][j] and map[i][j] == 1:
                graph(i, j)
                counter += 1

    print(f'Your maps shape is: {map.shape}, and it looks like this: \n {map}')

    return (f'Number of islands: {counter}\n')

# print(f'{islands(k)}\n')
# print(f'{islands(t)}\n')
print(f'{islands(p)}\n')
print(f'{islands(m)}\n')