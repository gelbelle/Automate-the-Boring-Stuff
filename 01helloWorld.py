#This program says hello and asks for your name

print("Hello world")
print("What is your name?")
myName = input()

print(f"It is nice to meet you, {myName}")
print(f"The length of your name is {len(myName)}")

print("What is your age?")
myAge = input()

print(f"You will be {int(myAge)+1} next year")