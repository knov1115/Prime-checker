n = int(input("Enter a number: "))
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, int(n**(0.5))+1):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
