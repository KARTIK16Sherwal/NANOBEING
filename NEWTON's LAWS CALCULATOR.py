print("Hello,User please tell us your so that we can know you better!")
name = input("Tell us your name: ")
print(f"Hello, {name} nice to meet you welcome Newton's laws of motion")
print("Tell us waht do you want.Type find in front of your value that you want to ask! and 'quit' to exit.")
F = input("FORCE(F): ")
M = input("MASS(M): ")
A = input("ACCELARATION(A): ")
while True:
    if F == 'find':
        ma = int(M) * int(A)
        print(ma)
        break

    if F == 'quit':
        print("Thanks for using us!")
        break
    
    if M == 'find':
        fa = int(F) / int(A)
        print(fa)
        break

    if M == 'quit':
        print("Thanks for using us!")
        break

    if A == 'find':
       fm = int(F) / int(M)
       print(fm)
       break

    if A == 'quit':
        print("Thanks for using us!")
        break
   
   
