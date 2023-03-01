tekst="alicja ma kota"
wzorzec="kot"
i=0
while (i<(len(tekst)-len(wzorzec))):
    j=0
    while(j<len(wzorzec) and wzorzec[j]==tekst[i+j]):
        j+=1
    if (j==len(wzorzec)):
        print("wzorzec znajduje się na miejscu ",i+1)
    i+=1