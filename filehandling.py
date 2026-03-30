
#file handling: is a way to store data permanently on disk. It allows us to read and write data to files, which can be used for various purposes such as saving user information, logging events, or storing application data.

#opening a file

file = open("file.txt", "r")

#reading a file

date=file.readlines()
print(date)
file.close()

#append mode

file=open("file.txt","a")
file.write("\nhiii i am anjali")
file.close()

#creating a file

f=open("demo.txt","x")
f.close()

#writing a file : write in file and delte the write content

f=open("file.txt","w")
f.write("hiiii mnnujjjijijnnn")
f.close()

#with :.close()or with used to close the file

with open("file.txt","r") as f:
    print(f.read())





