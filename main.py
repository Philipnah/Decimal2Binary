
number = int(input("\nDecimal number: "))

binary = []

while (number > 0):
	binary.append(number % 2)
	number = number//2
	

# [::-1] is used to reverse the array
print("\nBinary:" + "\n" + str(binary[::-1]))

for i in binary:
	print(i, end="")
print("\n")
