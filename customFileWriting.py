#this asks the user to create a filename for his choice
filename=str(input("Enter file name: "))
f=open(filename+".txt","w")
data=str(input("Enter the data to enter in the file : "))
f.write(data)
f.close()