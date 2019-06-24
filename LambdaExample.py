x = lambda a : a + 10
print(x(5)) 


y = lambda a : a * a * a
print(y(3))

z = lambda f, g : f in g
print(z("rl", "world!"))

examps = [1, 1, 3, 6, 5, 11]

map(lambda m : m * 3, examps)

s = lambda x: x.startswith('B')
print(s('Bob'))

