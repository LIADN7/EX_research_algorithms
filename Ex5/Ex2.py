

import queue

INF=100000


#min distance for dijkstra 
def min_distance(dist,queue):
    minimum = float(INF)
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index

# dijkstra algo
def dijkstra(graph, src):
    row = len(graph)
    col = len(graph[0])
    dist = [INF] * row
    dist[src] = 0
    queue = []
    for i in range(row):
        queue.append(i)
             
    #Find shortest path from src to all
    while queue:
        u = min_distance(dist,queue)
        queue.remove(u)
        for i in range(col):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
    return dist


def floyd_warshall(arr):
    n = len(arr)
    dist = list(map(lambda i: list(map(lambda j: j, i)), arr))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dist[i][j]>dist[k][j]+dist[i][k]):
                    dist[i][j]=dist[k][j]+dist[i][k]

    return dist



def shortest_path(arr, start: int = INF):
    if(start is INF):
        return floyd_warshall(arr)
    return dijkstra(arr, (start-1))








if __name__ == "__main__":

    arr = [[0,18,5,INF],
            [18,0,2,3],
            [5,2,0,INF],
            [INF,3,INF,0]]
    print("  <<<<Graph>>>>")            
    print("       18               ")
    print("   [1]----[2]                ")
    print("   |   /   \ 3                ")
    print("  5|  /2    \             ")
    print("   | /      [4]           ")
    print("   [3]                   ")
    print()
    print("send the array and get the path matrix of all the nodes")
    a = shortest_path(arr)
    for i in a:
        print(i)
    print()
    print("send the array and node number 1 and get all his path")
    print(shortest_path(arr,1))

