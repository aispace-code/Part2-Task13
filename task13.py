A = int(input("Enter the number: "))
print("Squares in the given range are:")
print([i ** 2 for i in range(1, A + 1) if i ** 2 <= A])