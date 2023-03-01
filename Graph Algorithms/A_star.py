def A(graph):
  listInd=[0]*len(graph)
  listwart=[0]*len(graph)
  indMin=0
  minWay=graph[0][0][0]+graph[0][0][1]
  stop=0
  while stop==0:
    try:
      minWay=graph[0][listInd[0]][0]+graph[0][listInd[0]][1]+listwart[0]-graph[0][listInd[0]-1][1]
      indMin=0
    except:
      minWay=graph[0][listInd[0]][0]+graph[0][listInd[0]][1]+listwart[0]
      indMin=0

    for z in range(len(graph)):
      i=listInd[z]
      try:
        if minWay>graph[z][i][1]+graph[z][i][0]-graph[z][i-1][1]+listwart[z]:
          minWay=graph[z][i][1]+graph[z][i][0]-graph[z][i-1][1]+listwart[z]
          indMin=z
      except:
        if minWay>graph[z][i][1]+graph[z][i][0]:
          minWay=graph[z][i][1]+graph[z][i][0]
          indMin=z
          
    listwart[indMin]+=graph[indMin][listInd[indMin]][0]+graph[indMin][listInd[indMin]][1]
    try:
      listwart[indMin]-=graph[indMin][listInd[indMin]-1][1]
    except:
      co=0

    listInd[indMin]+=1
    print("Wartosc sciezek: ")
    print(listwart)
    print("Ilosc krokow dla sciezki: ")
    print(listInd,"\n")
    for z in range(len(graph)):
      i=indMin
      j=listInd[z]
      if graph[z][j][0]==0:
        stop=1        
        print("\n\n        WYNIKI:\nNumer najkrotszej sciezki:")
        print(i)
        print("Najkrotsza sciezka:")
        print(graph[i])
        print("Wartosci sciezki")
        print(listwart[i])
        print("Dlugosc sciezki:")
        print(listInd[i])
graph=[
  [[1,7],[3,1],[14,4],[12,3],[53,3],[0]],
  [[1,2],[15,3],[4,5],[11,2],[0]]
]    
print(graph)
A(graph)