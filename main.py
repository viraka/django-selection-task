def add_n_natural_numbers(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total

n = int(input("Enter your desired number: "))
print("Sum of first",n,"natural numbers is",add_n_natural_numbers(n))