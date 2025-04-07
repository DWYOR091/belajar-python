import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
  
#mencari huruf keci a - m
a = re.findall("[a-m]", txt)
print(a)

#mencari digit karakter
digit = "harganya 50rb"
b = re.findall("\d", digit)
print(b)

greeting = "Hello Rifqi"
c = re.findall("^Hello", greeting)
if c:
    print("yes start with hello")
else:
    print("no match") 


#cari nama yg starnya he diikuti belakangnya huruf o
print(re.findall("He.*o", greeting))

print(re.findall("\AThe",txt))

#\D return yg tidak mengandung digit
print(re.findall("\D",digit))

f = re.split("\s", txt, 1)
print(f)
#menggantikan spasi jadi -
g = re.sub("\s", "-", txt)
print(g)

h = re.search("ai", txt)
print(h)