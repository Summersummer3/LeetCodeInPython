def f_1():
    a = 1
    b = 2
    print a + b

def f_2(n):
    for each in range(0,n):
        print each

def f_3(n):
    for i in range(0,n):
        for j in range(0,n):
            print i * j

def f_4(n):
    i = 0
    while 2**i < n:
        print 2**i
        i += 1
 
        
f_1()
print "\n"
f_2(10)
print "\n"
f_3(10)
print "\n"
f_4(10)