
number = int(input("decimal number: "))

binary = []

while (number > 0):
	binary.append(number % 2)
	number = number//2
	

print(binary.reverse())
