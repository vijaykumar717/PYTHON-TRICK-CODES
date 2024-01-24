file_creation=open('output.txt','w')

for i in range(1,11):
    output=i,'*2=',i*2
    file_creation.write(str(output)+'\n')

file_creation.close()
