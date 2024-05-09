# dict_hn={'A':10,'B':15,'C':20,'D':25,'E':30}
# dict_gn={
#     'A':{'B':10,'C':15,'D':14,'E':10},
#     'B':{'A':10,'C':15,'D':14,'E':10},
#     'C':{'B':10,'A':15,'D':14,'E':10},
#     'D':{'B':10,'C':15,'A':14,'E':10},
#     'E':{'B':10,'C':15,'D':14,'A':10},
# }

# start='A'
# goal='D'

# def getFn(citystr):
#     cities=citystr.split(',')
#     hn=dict_hn[cities[-1]]
#     gn=sum(dict_gn[cities[i]][cities[i+1]] for i in range(len(cities)-1))
#     return hn+gn

# def main():
#     cityq=[(getFn(start),start)]
#     while cityq:
#         total,citystr=cityq.pop(0)
#         thiscity=citystr.split(',')[-1]
#         if thiscity==goal:
#             result=citystr+'::'+str(total)
#             print("Result of A* is :-",result)
#             return
#         for i in  dict_gn[thiscity]:
#             cityq.append((getFn(citystr+','+i),citystr+','+i))
#         cityq.sort()

# main()



# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)
#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
#     def dfsUtil(self,v,visited):
#         visited[v]=True
#         print(v,end=" ")
#         for neighbour in self.graph[v]:
#             if not visited[neighbour]:
#                 self.dfsUtil(neighbour,visited)
#     def dfs(self,start):
#         visited=defaultdict(bool)
#         self.dfsUtil(start,visited)
#     def bfs(self,start):
#         visited=defaultdict(bool)
#         queue=[start]
#         while queue:
#             vertex=queue.pop(0)
#             if not visited[vertex]:
#                 print(vertex,end=' ')
#                 visited[vertex]=True
#                 for neighbour in self.graph[vertex]:
#                     if not visited[neighbour]:
#                         queue.append(neighbour)
#         print()

# g=Graph()
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(1,3)
# g.addEdge(1,4)
# g.addEdge(2,5)
# g.addEdge(2,6)
# g.addEdge(4,8)

# print("DFS is :-")
# g.dfs(0)
# print("\n")

# print("BFS is :-")
# g.bfs(0)
# print("\n")


# INR=9999999
# N=5
# G=[
#     [0,2,6,0,0],
#     [2,0,1,0,1],
#     [6,1,0,2,0],
#     [0,0,2,0,5],
#     [0,1,1,5,0]
# ]

# selectec_node=[False]*N
# selectec_node[0]=True

# print("Edge    Weight\n")
# for _ in range(N-1):
#     minimum=INR
#     a=b=0
#     for m in range(N):
#         if selectec_node[m]:
#             for n in range(N):
#                 if not selectec_node[n] and G[m][n] and G[m][n]<minimum:
#                     minimum=G[m][n]
#                     a,b=m,n
#     print(f"{a}-{b}:{G[a][b]}")
#     selectec_node[b]=True




def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')




greet('ZealBot', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
