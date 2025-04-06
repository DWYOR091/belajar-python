#match atau switch case di python

a = 12

match a:
    case 10:
        print("besar")
    case a if a < 5:
        print("kecil")
    case _:
        print("tidak ada")
        
        
#match day
day = 4
match day:
    case 1:
        print("senin")
    case 2:
        print("selasa")
    case 3:
        print("rabu")
    case 4:
        print("kamis")
    case 5:
        print("jum'at")
    case 6:
        print("sabtu")
    case 7:
        print("minggu")
    case _:
        print("Hohoho tidak ada")
        