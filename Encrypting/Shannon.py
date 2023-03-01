
kod = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": ""}
symbole = [(25, "A"), (15, "B"), (10, "C"), (10, "D"), (20, "E"),(20, "F")]
def shan(symbole):
    if len(symbole) > 1:
        symbole = sorted(symbole, reverse=True)
        l = []
        p = symbole
        sumal = 0
        sumap = 0
        for symbol in p:
            sumap += symbol[0]
        i=0
        while i < len(symbole):
            if abs((sumal+p[0][0]) - (sumap-p[0][0])) < abs(sumal - sumap):
                s = p.pop(0)
                l.append(s)
                sumap -= s[0]
                sumal += s[0]                
                i+=1
            else: break        
        for symbol in p:
            kod[symbol[1]] += "1"
        for symbol in l:
            kod[symbol[1]] += "0"
        shan(l) 
        shan(p)
shan(symbole)
print("Pokazany kod: ", kod)
tekst = "CADE"
print("Tekst: ", tekst)
print("Kod tekstu: ", end="")
for litera in tekst:
    print(kod[litera], end="")