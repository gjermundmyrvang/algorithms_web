

n = 0

x = 0
for i in range(n):
    for j in range(i):
        x += 1



def toTheMoon(n):
    print("ALMOST THERE")
    for i in range(n):
        for j in range(i):
            toTheMoon(n-j)
    print("FINALLY")


def whatsMyOnotation(n):
    if n <= 0:
        return
    xyz = n//2
    whatsMyOnotation(xyz)


def loops(n):
    output = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        output = not output
    return output

def whatsGoingOnHere(n, m, k, l):
    for i in range(n):
        for j in range(m):
            print(j + "   O   " + m)
    
    for numb in range(k):
        for element in range(l):
            print(k + "   IOI   " + l)
    
    

def wtf(n):
    if n < 1:
        return
    n -= 1
    for i in range(n):
        wtf(n//n)


def trickyOne(n):
    n = 2^n
    for number in range(-1000, 1000000):
        n = n-1
        print(n + number)



