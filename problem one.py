number = int(input())
product_of_digits = 1
while number != 0:
    digit = number % 10
    if digit != 0:
        product_of_digits *= digit
    number //= 10
print(product_of_digits)
