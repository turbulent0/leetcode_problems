nums = [-2, -1, 3, 4]
neg = list(filter(lambda x: x < 0, nums))
pos = list(filter(lambda x: x >= 0, nums[::-1]))

res = []
# add numbers while neg and pos are not empty
while neg and pos:     
    res.append(pos.pop() ** 2) if abs(neg[-1]) > abs(pos[-1]) else res.append(neg.pop() **2)
# add all values from not empty array
temp = neg if neg else pos
_ = [res.append(temp.pop() ** 2) for _ in range(len(temp))]

