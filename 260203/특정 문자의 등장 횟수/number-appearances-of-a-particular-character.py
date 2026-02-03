a = input()


e = True
num_ee = 0
num_eb = 0
a_new = a

while a_new:
    if 'ee' in a_new:
        s = a_new.find('ee')
        a_new = a_new[s+1:]
        num_ee += 1
    else:
        break

a_new = a

while a_new:
    if 'eb' in a_new:
        s = a_new.find('eb')
        a_new = a_new[s+1:]
        num_eb += 1
    else:
        break
print(num_ee, num_eb)