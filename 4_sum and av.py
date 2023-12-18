'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 4              ####
####     EXPERIMENT NAME: SUM AND AVG  ####
####                                   ####
###########################################
###########################################

'''

size=int(input("how many numbers :"))
array=[]
for i in range (0,size):
	num=input()
	array.append(num)

sum=0
for i in array:
	sum=sum+int(i)

print("SUM is ",sum)
print("AVG is ",sum/size)

'''
###########################################
###########################################
             
              OUTPUT


how many numbers :10
43
64
2
5
6
34
123
54
3
5
SUM is  339
AVG is  33.9

###########################################
###########################################

'''
