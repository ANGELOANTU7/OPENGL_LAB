
'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 6              ####
####     EXPERIMENT NAME:ALPHABETIC    ####
####                                   ####
###########################################
###########################################

'''

n=int(input())
list_n=[]
for i in range (0,n):
	list_n.append(input())

list_n.sort()

print("ORDERED LIST")
for name in list_n:
	print(name)



'''
###########################################
###########################################
             
              OUTPUT


10

Angelo
Rahul
Simon
Theertha
Punya
Ronaldo
Messi
Subhas
Pramod
Dell


ORDERED LIST
Angelo
Dell
Messi
Pramod
Punya
Rahul
Ronaldo
Simon
Subhas
Theertha



###########################################
###########################################

'''

