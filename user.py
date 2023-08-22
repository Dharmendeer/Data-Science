import numpy as np

arr1= np.zeros((3,4))

for i in range(0,3):
    for j in range(0,3):
        arr1[i][j]=int(input("Enter vale of arr1:  "))
print(arr1)

arr2=np.zeros((3,4))

for i in range(0,3):
    for j in range(0,3):
        arr2[i][j]=int(input("Enter vale of arr2:  "))
print(arr2)



print("Conctenate of two array horizantly: ")
concat_hori=np.concatenate((arr1,arr2),axis=1)
print(concat_hori)

print("Conctenate of two array vertically: ")
concat_vert=np.concatenate((arr1,arr2),axis=0)
print(concat_vert)

print("Sort of two array Horizantly: ")
sort_hori=np.sort((arr1,arr2),axis=1)
print(sort_hori)

print("Sort of two array vertically: ")
sort_vert=np.sort((arr1,arr2),axis=0)
print(sort_vert)