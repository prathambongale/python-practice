spam_amount = 0 # valiable assignment - assigning value 0 to spam_amount using =, which is assignment operator 
# No need to declare varibale before assignment like Java or C++.
# No need to define datatype for varibale. Varibale can store any value.

print(spam_amount) # use to display value on console that is pass to it

spam_amount = spam_amount + 4   # reassignment of value

if spam_amount > 0:
    print("But I don't wamt AMY spam!")

viking_song = "Spam " * spam_amount
print(viking_song) # This will print "Spam Spam Spam Spam"

viking_song = 4 * spam_amount
print(viking_song) # This will print "16"
# operators like * and + have a different meaning depending on what kind of thing they're applied to. (The technical term for this is operator overloading)

print("")
print("")
print("---------------------------------------")
print("")
print("")
# Data Types: Number, Float

# Operations: Number

a = 10
b = 6
print("Value of a: ")
print(a)
print("Value of b: ")
print(b)

print("")
print("")

# Additions
print("Addition :")
print("a + b = ")
print(a + b)

print("")

# Subtraction
print("Subtraction :")
print("a - b = ")
print(a - b)

print("")

# Multiplication
print("Multiplication :")
print("a * b = ")
print(a * b)

print("")

# True Division
print("True Division :")
print("a / b = ")
print(a / b)

print("")

# Floor Division
print("Floor Division (remove fractional part):")
print("a // b = ")
print(a // b)

print("")

# Modulus
print("Modulus:")
print("a % b = ")
print(a % b)

print("")

# Exponentiation
print("Exponentiation:")
print("a ** b = ")
print(a ** b)

print("")

# Negation
print("Negation:")
print("-a = ")
print(-a)

print("")

# Operations get executed in "PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction" order

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
print("")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)
print("")

# Build in functions
print(min(10,52,87))
print(max(10,52,87))
print("")

# Absolute value
print(abs(89.0))
print(abs(-89.0))
print(abs(89))
print(abs(-89))
print("")

print(float(115))
print(int(7.8956))
print("")

print(float(10.8) + 10.2)
print("")