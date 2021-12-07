a=int(input("Enter first no."))
b=int(input("Ente the second no."))
print("Before Swapping")
print("a : {}".format(a))
print("b : {}".format(b))
a=a+b
b=a-b
a=a-b
print("After Swapping")
print("a : {}".format(a))
print("b : {}".format(b))