f=open("nevezetessegek.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)
f.close()

def datumcucc():
    bemenet=int(input("Adj meg egy dátumot: "))
    for i in range(0,len(nagylista)):
        if bemenet==int(nagylista[i][2]):
            print(nagylista[i][0])
    
def orszagcucc():
    calc=0
    bemenet=input("Adj meg egy országot: ")
    for i in range(0,len(nagylista)):
        if bemenet==nagylista[i][1]:
            calc+=1
            print(nagylista[i][0])
    if calc==0:
        print("nincs ilyen")
    calc=0


def nevezetessegcucc():
    bemenet=input("Adj meg egy nevezetességnevet: ")
    for i in range(0,len(nagylista)):
        if bemenet==nagylista[i][0]:
            print(nagylista[i][1],nagylista[i][2])


print("1,Dátum szerinti keresés\n2,Ország szerinti keresés\n3,Név szerinti keresés")
while True:
    try:
        bemenet=int(input("válasz: "))
        if bemenet==1:
            datumcucc()
            break
        if bemenet==2:
            orszagcucc()
            break
        if bemenet==3:
            nevezetessegcucc()
            break
        else:
            raise ValueError
    except ValueError:
        print("Nincs ilyen lehetőség!")
