import math



def mainmenu(label):
    prompt = "\tMásodfokú-1  ---- elsőfokú-2:  "
    x = str(input(prompt))
    if(x == "1"):
        f1(label)
    if(x == "2"):
        f2(label)
    


def f1(label):
    print(label)
    txt = "\tVan-e megoldása a másodfokú egyenletnek?"
    print(txt)
    a = int(input("Kérem az a együtthatót: ") )
    b = int(input("Kérem a b együtthatót: ") )
    c = int(input("Kérem a c együtthatót: ") )

    diszkriminans = b*b - 4*a*c 

    if (diszkriminans == 0):
        print(-b/(a*2))

        txt = "\tAz egyenletnek egy megoldása van. "

        print(txt)



    else:
        if (diszkriminans < 0):
            txt = "\tAz egyenletnek nincs megoldása. "
            print(txt)
        else:
            print("\tAz egyenletnek két megoldása van. ")
            print("\tMegoldás: ", (-b- math.sqrt(diszkriminans))/(2*a))
            print("\tMegoldás: ", (-b+ math.sqrt(diszkriminans))/(2*a))
    prompt = "\tMásodfokú-1  ---- elsőfokú-2:  "
    x = str(input(prompt))
    if(x == "1"):
        f1(label)
    if(x == "2"):
        f2(label)


def f2(label):
    print(label)
    
    


    a = int(input("Kérem az a-t: ") )
    b = int(input("Kérem a b-t: ") )

    if(a != 0):
        txt =  "Megoldás:"        + str(-b/a)
        print(txt)

    else:
        if(b != 0):
            txt = "Az egyenlet nem megoldtható"
            print(txt)
        else:
            txt = "Az egyenletnek a megoldása az összes valós szám"
            print(txt)

    prompt = "\tMásodfokú-1  ---- elsőfokú-2:  "
    x = str(input(prompt))
    if(x == "1"):
        f1(label)
    if(x == "2"):
        f2(label)
   




    





mainmenu("menű")
