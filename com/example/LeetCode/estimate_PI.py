import random

def estimate_PI(N):
    n = 0
    for i in range(0,N):
        x = random.random()
        y = random.random()
        if (x**2+y**2)<1:
            n += 1
    return 4.0 * (float(n)/float(N))

print estimate_PI(10000)
print estimate_PI(100000)
print estimate_PI(1000000)
    