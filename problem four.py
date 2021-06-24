number = int(input())
sum_of_digits=0
i = True
while i:
    while number != 0:
        sum_of_digits+=(number%10)
        number//=10
    if sum_of_digits<10:
        i = False
    number = sum_of_digits
print(sum_of_digits)

