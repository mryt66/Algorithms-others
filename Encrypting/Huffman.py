kod = {"A":"", "B":"", "C":"", "D":"", "E":"", "F":""}
symbole = [(35, "A"), (5, "B"), (10, "C"), (20, "D"), (25, "E"), (5, "F")]
symbole = sorted(symbole, reverse=True)
while len(symbole) > 1:
    s1 = symbole.pop()
    s2 = symbole.pop()
    for i in s1[1]:
        kod[i] = "0" + kod[i]
    for i in s2[1]:
        kod[i] = "1" + kod[i]
    s1s2 = (s1[0]+s2[0], s1[1]+s2[1])
    symbole.append(s1s2)
    symbole = sorted(symbole, reverse=True)
tekst = "CEDA"
print("Tekst: ", tekst)
print("Kod tekstu: ", end="")
for i in tekst:
    print(kod[i], end="")