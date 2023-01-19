print("write your values: ")
print("")
a = int(input("what is your a value: "))
b = int(input("what is your b value: "))
c = int(input("what is your c value: "))
minb = -1*b
d = (b * b - 4*a*c)
if d < 0:
    print("no real root are possible")
    quit()
elif d == 0:
    print("root are real and equal")
elif d> 0:
    print("routes are real and not equal")
    
x1 = (minb + d**0.5)  / 2*a  
x2 = (minb - (b * b - 4*a*c)**0.5)  / 2*a
print(f"answers are x1:{x1}")
print(f"answers are x2:{x2}")