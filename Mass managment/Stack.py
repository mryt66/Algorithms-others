#stos
stos=[]
max=3
def isempty(stos):
    if not stos:
        return True
    else:
        return False

def Pop(stos):#usuń ze stosu
    if isempty(stos)==True:
        print("nie mozna usunac elementu")
    else:
        x=slice(0,len(stos)-1)
        return stos[x]

def Push(stos,el,max): #dodaj na stos
    if isempty(stos)==False:
        x=len(stos)
        if x>=max:
            stos=Pop(stos)
            stos = stos + [el]
        else:
            stos = stos + [el]
    if isempty(stos)==True:
        stos=[1]
        stos[0]=el
    print(stos)
    return stos
stos=Pop(stos)
stos=Push(stos,1,max)
stos=Push(stos,2,max)
stos=Push(stos,3,max)
stos=Push(stos,4,max)
stos=Pop(stos)
print(stos)



