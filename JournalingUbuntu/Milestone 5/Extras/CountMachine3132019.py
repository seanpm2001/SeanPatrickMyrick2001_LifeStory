# start of program
print ("Count loop")
x = int(input("Enter a starting number: "))
y = int(input("Enter a stopping number: "))
if (x > y): 
	x = y 
	y = x
if (y < x):
	y = x
	x = y
for i in range  (x, y):
	print (str(i))
print (str(i))
noMore = input("Thank you for counting with me!")
# end of program