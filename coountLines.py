#this program count the number of line of the file
f=open('sample.txt','r')
print(len(f.read().split('\n')))
f.close()