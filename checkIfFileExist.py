import os,sys
if os.path.isfile("3.txt"):
    r_file=open("3.txt","r")
    data=r_file.read()
    print(f"the data in the file is {data}")
    r_file.close()
else:
    print("the file does not exist")
    sys.exit()