hello = "Hello, World FUN! \t kocak"
#capitalize jadi didepannya saja huruf besar
print(hello.capitalize())
print(hello.casefold())
print(hello.center(50, "-"))
print(hello.count("o",1,3)) 
print(hello.encode())
print(hello.endswith("o",1,5)) #menghasilkan nilai true atau false jika string diakhir sama
print(hello.expandtabs(30)) #atur jarak tabs
print(hello.find("!")) #return posisi index
uang = "{} for only Rp.{rupiah}"
print(uang.format("makanan",rupiah = 2000)) 
print(hello.index("!"))
print(hello.isalnum())
print(hello.isalpha())
a = "   \\t asdas adsa"
print(a.isascii())
tes = "123"
print(tes.isnumeric())
myTuple = ("Aku","Suka","Makanan")
print(" ".join(myTuple))
txt = "kocak,gaming"
print(txt.rsplit(","))
print(hello.title())
print(hello.swapcase())
