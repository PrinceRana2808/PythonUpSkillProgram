#From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]

list=[1,2,3,4,5]
new_list=[]
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if(i+j==9):
            list.append(i)
            list.append(j)
            break
print(new_list)