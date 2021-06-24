number = int(input())
number = number - 1
i = True
k = False
copy_of_number = number
while i:
    if number %3 == 0:
        while number!=0:
            if number %3 == 0:
                number = number // 3
            else:
                copy_of_number -= 1
                number = 0
            k = True
        if k is True:
            i = False
        number = copy_of_number
    else:
        number -= 1 
        copy_of_number = number
print(copy_of_number)
