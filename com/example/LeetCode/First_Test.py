def foo(x):
    return True if x > 10 else False

print foo(10)

print ["a",] + ["b","c"]
a = [0]
a.extend([1,2])
print a

a = []
import random
for i in range(10):
    a.append(random.randint(0,10))

print a