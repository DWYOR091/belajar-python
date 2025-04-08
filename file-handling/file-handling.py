#read file
f = open('test.txt', 'r')
print(f.read())

#write/create file with a
f2 = open('test2.txt','a')
f2.write("hello rifqi")
f2.close()

fopen2 = open("test2.txt","r")
print(fopen2.read())

f3 = open("test3.txt","w")
f3.write("kocak gaming!")
f3.close()

fopen3 = open("test3.txt","r")
print(fopen3.read())