# Operasi NOT
print("==NOT==")

a = True
b = not a

print("data a : ",a)
print("b = not a")
print("data b : ",b)

# Operasi AND
print("==AND==")
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)
x = True
y = False
z = x and y
print(x, 'and', y, '=', z)
x = False
y = True
z = x and y
print(x, 'and', y, '=', z)
x = False
y = False
z = x and y
print(x, 'and', y, '=', z)

# Operasi OR
print("==OR==")
x = True
y = True
z = x or y
print(x, 'Or', y, '=', z)
x = True
y = False
z = x or y
print(x, 'Or', y, '=', z)
x = False
y = True
z = x or y
print(x, 'Or', y, '=', z)
x = False
y = False
z = x or y
print(x, 'Or', y, '=', z)

# Operasi XOR
print("==XOR==")
x = True
y = True
z = x ^ y
print(x, 'xor', y, '=', z)
x = True
y = False
z = x ^ y
print(x, 'xor', y, '=', z)
x = False
y = True
z = x ^ y
print(x, 'xor', y, '=', z)
x = False
y = False
z = x ^ y
print(x, 'xor', y, '=', z)
