print("HI")
print("BYE")
print("compile time error,mostly wrong syntax nd spelling mistake")

a=10
b=20
print(a+a,"logical error")

try:
    a=int(input())
    b=int(input())
    print(a+b,"runtime error which is value error bcz in this case instead of integer alphabet is given")
except Exception :
    print("probelm to solve runtime error",e)

finally :
    print("Done")
