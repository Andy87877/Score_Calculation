a = [4,3.5,4,2,2,2,2,0.5] # 加權
l1 = [71,61,88,83,67,84,86,58] #我
#l2 = [79,67,61,60,68,86,84,70] #莊
#l3 = [81,77,53,76,77,80,78,76] #林

total = 0

for i in range(len(l1)):
    total += l1[i]*a[i]
avg = total/sum(a)
print("Total:",total)
print("Avg:",avg)
