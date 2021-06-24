a = int(input())
b = int(input())
c = int(input())
import math
if (a+b>c):
    if (b+c>a):
        if(a+c>b):
            if a**2+b**2 == c**2:
                print("right triangle")
            elif b**2+c**2 == a**2:
                print("right triangle")
            elif a**2+c**2 == b**2:
                print("right triangle")
            else:
                if math.acos((a**2+b**2-c**2)/(2*a*b))> (math.pi/2):
                    print("abtuse triangle")
                else: 
                    if math.acos((a**2+c**2-b**2)/(2*a*c))> (math.pi/2):
                        print("abtuse triangle")
                    else: 
                        if math.acos((b**2+c**2-a**2)/(2*b*c))> (math.pi/2):
                            print("abtuse triangle")
                        else: 
                            print("acute triang")
        else:
            print("No triange")
    else:
        print("No triange")

else:
    print("No triangle")

