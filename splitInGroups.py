import random

skupiny = {}

def createGroups():
  a = int(input("počet skupin" + "\n"))
  i = 1
  for x in range(1,a+1):  #vytvoření skupin
     skupiny['skupina '+str(x)] = None
     i = i+1

def insertPeople():
  listSkupin = []
  lidé = []
  
  b = int(input("počet lidí" + "\n"))
  for x in range(1,b+1):
    lidé.append(x)
  random.shuffle(lidé)
  
  n=0
  while n<len(skupiny):
    listSkupin.append([])
    n += 1

  m=0
  for x in lidé:
    listSkupin[m].append(x)
    if m < len(listSkupin)-1:
      m += 1
    elif m == len(listSkupin)-1:
      m = 0
    else:
      continue
    
  print(listSkupin)

  l=1
  k=0
  while l<=len(listSkupin):
    skupiny['skupina '+str(l)]=listSkupin[k]
    l += 1
    k += 1

  print(skupiny)
    
 

  
  

createGroups()
insertPeople()

  
