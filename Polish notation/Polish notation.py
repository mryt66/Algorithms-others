x="3;2.1;3.5;1.1"
l1=x.split(";")
temp1=l1[0]
for i in l1:
    if i>temp1:
        temp1=i
print(temp1)

b="6 3 4 + * 5 *" #6*(3+4)*5
def ONPdoN(a):
   stos=[]
   for i in a:
       if i == " ":
           continue
       if i>"0"and i<="9":
           stos.insert(0,i)
       else:
           c=stos[0]
           stos.pop(0)
           d=stos[0]
           stos.pop(0)
           stos.insert(0,"("+d+i+c+")")
   print(stos[0])
ONPdoN(b)

def wartosci(wyr):
   for i in range(len(wyr)):
       if wyr[i]=='+' or wyr[i]=='-':
           return 1
       elif wyr[i]=='/' or wyr[i]=='*':
           return 2
       elif wyr[i]=='^':
           return 3
       else:
           return 0

def dzialaj(a):
 wyjscie=""
 stos1=[]
 for i in range(len(a)):
   if a[i].isdigit():
     if(i!=len(a)-1):
       if a[i+1].isdigit():
         wyjscie+=a[i]
       else:
         wyjscie+=a[i]+" "
     else:
       wyjscie+=a[i]+" "
   elif a[i]=="(":
     stos1.insert(0, "(")
   elif a[i]==")":
     for j in stos1:
       if j != "(":
         wyjscie+=j+" "
       else:
         break
   else:
     if len(stos1)!=0:
       while wartosci(stos1[0]) >= wartosci(a[i]):
         if stos1[0]!="(":
           wyjscie+=stos1[0]+" "
         stos1.pop(0)
         if len(stos1)==0:
           break
       stos1.insert(0, a[i])
     else:
       stos1.insert(0, a[i])
 for i in stos1:
   if i!="(":
     wyjscie+=i+" "
 print(wyjscie)

a="3+4/5+4"
dzialaj(a)















