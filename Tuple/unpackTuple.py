#unpacking tuple sama dengan desctructuring di jaavascript
fruits = ("banana","avocado","apple","strawbeery","blueberry")
(a,b,c,d,e) = fruits
print(a)
print(b)
print(c)
print(d)

#use asterisk 
(kuning,hijau,*merah) = fruits
print(kuning)
print(hijau)
print(merah) #menjadi array / lists