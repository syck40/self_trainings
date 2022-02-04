l1 = [1,2,3,4]
def cal(l1):
    print(len(l1))
    times = 0
    for n in l1:
        for n1 in l1:
            print(f"1st is {n}, 2nd is {n1}")
            times += 1
    print(times)
cal(l1*2)
