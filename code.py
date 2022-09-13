limit = 10
sum = 0

for i in range(limit) :
	num = float(input("Escribe un número:" ))
	sum += num
	print(f"El valor de i es: {i}")

print(f"El promedio es: {sum/limit}")
