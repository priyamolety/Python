# l=int(input("enter the length "))
# b=int(input("enter the breadth "))
# h=int(input("enter the height "))

# for i in range(l):
# 	print ("[", end = " ")
# 	for j in range(b):
# 		print("[" , end =" ")
# 		print("[", end =" ")
# 		for k in range(h): 

# 			print("*", end = " ") 
# 		print("] " )
# 		print(",")
# 		print ("\n")
# 	print ("]")
# print ("]")
# 					


from pprint import pprint
data = input("enter the dimensions ")

l,m,n = list(map(int,data.split()))

maat = [[['*' for i in range (n)] for j in range(m)] for k in range(l)]

pprint (maat)