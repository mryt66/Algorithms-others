def karp(string,pat):
    string = string.upper()
    pat = pat.upper()
    l = len(string)
    lp = len(pat)
    con = 13
    ch = 0 
    h= 0  
    for i in range(lp):
        ch += (ord(string[i])-ord('A')+1)*(con**(lp-i-1)) 
        h+= (ord(pat[i])-ord('A')+1)*(con**(lp-i-1))
    for j in range(l-lp+1):
        if j!=0:
            ch = con*(ch-((ord(string[j-1])-ord('A')+1)*(con**(lp-1))))+(ord(string[j+lp-1])-ord('A')+1)
        if(ch==h):
            print ("Znaleziono wzorzec na miejscu",j+1)
karp("abbacdsadasasdaaaa","sa")