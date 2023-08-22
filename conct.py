import numpy as np
l1=[[1,2,3],[5,6,8],[8,5,2]]
arr1= np.array(l1)
l2=[[1,2,5],[8,9,7],[9,6,4]]
arr2=np.array(l2)

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