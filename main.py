import math



def f1(label):
    print(label)
    txt = "\tVan-e megoldása a másodfokú egyenletnek?"
    print(txt)
    a = int(input("Kérem az a együtthatót: ") )
    b = int(input("Kérem a b együtthatót: ") )
    c = int(input("Kérem a c együtthatót: ") )

    diszkriminans = b*b - 4*a*c

    if (diszkriminans == 0):
        txt = "\tAz egyenletnek egy megoldása van. "
        print(txt)
    else:
        if (diszkriminans < 0):
            txt = "\tAz egyenletnek nincs megoldása. "
            print(txt)
        else:
            txt = "\tAz egyenletnek két megoldása van. "
            print(txt)







f1("1.feladat")
