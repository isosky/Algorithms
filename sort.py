import random
def sort_sc(array):
	if len(array)==0:
		return "length equals 0"
	if len(array)==1:
		return array
	for i in range(1,len(array)):
		for j in range(0,i):
			if array[i]<array[j]:
				c=array[i]
				array[i]=array[j]
				array[j]=c
	return array

def merge_sort(array_a,array_b):
	i=0
	j=0
	array_c=[]
	while i<len(array_a) and j<len(array_b):
		if array_a[i]<=array_b[j]:
			array_c.append(array_a[i])
			i+=1
		elif array_a[i]>array_b[j]:
			array_c.append(array_b[j])
			j+=1
	if i<len(array_a):
		for i in range(i,len(array_a)):
			array_c.append(array_a[i])
	if j<len(array_b):
		for j in range(j,len(array_b)):
			array_c.append(array_b[j])
	return array_c

def create_list(length,min,max):
	if min>=max:
		return "get random list wrong"
	arr=[]
	for i in range(0,length):
		arr.append(round(random.uniform(min, max),2))
	return arr

# def sort(array):
# 	if len(array)>100:
# 		return merge_sort(sort_sc(array(0,len(array)/2)))

aa=sort_sc(create_list(3,0,30))
print aa
ab=sort_sc(create_list(3,0,30))
print ab 



print merge_sort(aa,ab)