Alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alph1 = list(map(str,Alph))
#print(Alph1)

rangee = int(input("Enter rows:"))
p = 0
q = 1
letters = ((rangee)*(rangee + 1))//2
if letters > 26:
    Alph *= (letters//26) + 1
    Alph1 = list(map(str,Alph))
for i in range(rangee):
    q = p + i+ 1
    print(Alph[p:q])
    p += i + 1
