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
    
#Ezt a Milán csinálta!

bemenet=input("Adj meg egy országot: ")
for i in range(0,len(nagylista)):
    if bemenet==nagylista[i][1]:
        calc+=1
        print(nagylista[i][0])
if calc==0:
    print("nincs ilyen")
calc=0
