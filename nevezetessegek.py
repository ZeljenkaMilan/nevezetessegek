f=open("nevezetessegek.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)
f.close()

#Ezt a Kevin csinálta!
bemenet=int(input("Adj meg egy dátumot: "))
for i in range(0,len(nagylista)):
    if bemenet==int(nagylista[i][2]):
        print(nagylista[i][0])
    
