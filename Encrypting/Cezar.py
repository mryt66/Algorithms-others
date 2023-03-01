przes=-5
alfabet="ABCDEFGHIJKLMNOPRSTUWXYZ"
cezar=[]
if przes>0:
    for i in range(len(alfabet)):
        if (i+przes==len(alfabet)-1):
            j=0
            for j in range(przes):
                cezar.append(alfabet[j])
            break
        cezar.append(alfabet[i+przes])
elif przes<0:
    for i in range(len(alfabet)+przes,2*(len(alfabet))):
        if i>=len(alfabet):
            if alfabet[i-len(alfabet)] in cezar:
                break
            cezar.append(alfabet[i-len(alfabet)])
        else:
            cezar.append(alfabet[i])
elif przes==0:
    for i in alfabet:
        cezar.append(i)
print(cezar)


