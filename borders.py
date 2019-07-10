
import os

# borders.csv is the file with borders
with open("borders.csv") as f:
    content = f.readlines()

graph = {}

for l in content:
    line = l.strip()
    u = line.split(',')
    (name,neighbour) = u
    
    if name not in graph:
        graph[name] = [neighbour]
    elif neighbour not in graph[name]:
        graph[name].append(neighbour)
    
    #assume it's an directed graph
    if neighbour not in graph:
        graph[neighbour] = [name]
    elif name not in graph[neighbour]:
        graph[neighbour].append(name)

lista_panstw = graph.keys()

ultimate_list = []

for country in lista_panstw:
    distances = {}
    distances[country] = 0
    stack = [country]
    dist = 1
    while len(stack)>0:
        newstack = []
        for x in stack:
            for n in graph[x]:
                if n not in distances:
                    newstack.append(n)
                    distances[n] = dist
        if len(newstack) == 0:
            break
        stack = newstack
        dist+=1
    ultimate_list.append([country,stack,dist])

#sort list by farthest distance
ultimate_list.sort(key=lambda x:x[2])

for x in ultimate_list:
    print(x[0]+': '+str(x[1])+'; distance: '+str(x[2]-1))
    





