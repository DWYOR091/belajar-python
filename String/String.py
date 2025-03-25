#quotes di dalam quotes
myName = "It's Rifqi"
print(myName)

#assign string ke variable
a = "test"
print(a)

#multi line string
multiLine = """
Hello nama saya muhamad rifqi.
Saya sedang belajar bahasa pemrograman python.
"""
print(multiLine)

#string are arrays
#get char position
test = "Rifqi"
print(test[1] + "\n")

#loop through string 
for x in "kocak gaming":
    print(x)
    
#mendapatkan panjang string pakai len
print("\n",len(test))

#check string
print("Rif" in test)
#not
print("Kocak" not in test) #true
# pakai if
if "Rifq" in test:
    print("ada")
else:
    print("tidak ada")