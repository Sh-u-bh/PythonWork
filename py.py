'''
print("Hello World")
print("Hello World")
count = 0
for i in range (1,10):
    if i % 2 == 0:
        count+=1
        print(i)
print(f"We have {count} numbers")
def greet(firstName , Lastname):
    print(f"Hello {firstName} {Lastname}")
    print("Shubham Here this side")

greet("Shubham" , "Chandegara")

def get_greet(name):
    print (f"Hi {name}")

print(get_greet("Shubham "))
'''
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number 
        return total
print ("Start")
print (multiply(1, 2, 3))

