'''
###########################################
###########################################
####                                   ####
####     NAME :ANGELO ANTU             ####
####     ROLL NO: 20221017             ####
####     CLASS : CSA                   ####
####     EXPERIMENT NO: 1              ####
####     EXPERIMENT NAME: AREA         ####
####                                   ####
###########################################
###########################################

'''

def main():
	while(True):
		choice=int(input("Calculate Area of 1)Rectangle 2)Triangle 3)Exit"))
		if(choice==1):
			length=int(input("Enter length :"))
			breath=int(input("Enter breath :"))
			print("Area of Rectangle is ",length*breath)
		if(choice==2):
			length=int(input("Enter length :"))
			breath=int(input("Enter breath :"))
			print("Area of Triangle is ",length*breath/2)
		if(choice==3):
			exit()

main()

'''
###########################################
###########################################
             
              OUTPUT

Calculate Area of 1)Rectangle 2)Triangle 3)Exit1
Enter length :34
Enter breath :23
Area of Rectangle is  782
Calculate Area of 1)Rectangle 2)Triangle 3)Exit2
Enter length :50
Enter breath :2
Area of Triangle is  50.0
Calculate Area of 1)Rectangle 2)Triangle 3)Exit3

###########################################
###########################################

'''
