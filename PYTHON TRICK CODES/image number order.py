import os
os.chdir('imagelocation')
i=1
for file in os.listdir():
    src=file
    dst="img name"="_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1
