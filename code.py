x = 10
sum = 0

for i in range(x) :
	num = float(input("Escribe un número:" ))
	sum += num
	print(f"El valor de i es: {i}")

print(f"El promedio es: {sum/x}")
