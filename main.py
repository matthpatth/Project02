import random
count = 0 #number of generations
ksi = 0 #random values (gauss)
over = 0 #number of random values > 2
under = 0 #number of random values <-2
overlist = []
underlist = []
while count < 10000:
    n = random.normalvariate(0,1)
    count = count + 1
    if n >= 2:
        over = over + 1
        overlist.append(n)
    elif n <= -2:
        under = under + 1
        underlist.append(n)

print(over)
print(under)
print(abs(under-over))
print('Больше двух: ',overlist)
print('Менье двух: ',underlist)