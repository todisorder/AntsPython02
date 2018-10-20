from multiprocessing import Pool

def doubler(number1,number2):
    return number1 * number2

def tre(n):
    return 3*n

if __name__ == '__main__':
    numbers1 = [5, 10, 20]
    numbers2 = [2, 1, 3]
    numbers = [(1,2),(2,3),(4,5)]
    pool = Pool(processes=3)
    t=[((1,2))]
    a = pool.starmap(doubler, numbers)
    print(a)

    iter = 32
    b = list(range(10))
    c = [(i,iter) for i in b]
    pool = Pool(processes = 10)
    d = pool.starmap(doubler,c)
    print(d)


