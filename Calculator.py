Num1 = int(input("Number1: "))
Op = input("Operator: ")
Num2 = int(input("Num2: "))

if "*" in Op:
	product = Num1 * Num2
	print(product)

if "+" in Op:
	sun = Num1 + Num2
	print(sun)


if "-" in Op:
	difference = Num1 - Num2
	print(difference)


if "/" in Op:
	Quotient = Num1 / Num2
	print(Quotient)
