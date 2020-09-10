
choice = input("Please choose a conversion:\n1: Decimal to binary\n2: Decimal to hexadecimal\n3: Binary to decimal\n4: Hexadecimal to decimal\n5: Binary to hexadecimal\n6: Hexadecimal to binary\n\n: ")


if choice == "1":
	d2b()
elif choice == "2":
	d2h()
elif choice == "3":
	b2d()
elif choice == "4":
	h2d()
elif choice == "5":
	b2h()
elif choice == "6":
	h2b()
else:
	print("Your selection was not in the register. Please choose another option.")


def d2b():
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

def d2h():
	pass

def b2d():
	pass

def h2d():
	pass

def b2h():
	pass

def h2b():
	pass