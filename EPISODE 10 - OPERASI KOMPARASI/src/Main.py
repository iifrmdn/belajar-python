a = 10
b = 2

hasil = a > b
print(a, '>', b, '=', hasil)

hasil = a < b
print(a, '<', b, '=', hasil)

hasil = a >= b
print(a, '>=', b, '=', hasil)

hasil = a <= b
print(a, '<=', b, '=', hasil)

hasil = a == b
print(a, '==', b, '=', hasil)

hasil = a != b
print(a, '!=', b, '=', hasil)

x = 5
y = 5

# membandingkan alamat memori

print('nilai x = ', x, '=', hex(id(x)))
print('nilai y = ', y, '=', hex(id(y)))

hasil = x is y
print(x, 'is', y, '=', hasil)

hasil = x is not y
print(x, 'is not', y, '=', hasil)