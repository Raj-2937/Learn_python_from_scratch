#   File IO
#Python can be used to perform operations on a file. ( read and write data).

# Types of all files:
# 1. Text files: .txt, .doc, .docx, .log, etc.
# 2. Binary files:  .mp4, .mov, .png, .jpg, PEG, etc.

# Open ,read & colse.


f = open("demo.txt" ,"r")
data = f.read()
print(data)
print(type(data))
f.close()


f.write(" i want to learn java script")

with open("practice.txt" , 'w') as f:
    f.write("hi everyone\n we are learing file I\O\n")
    f.write("using Java.\n I link programing in Java")
    
