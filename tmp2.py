
string = input()
sum = 0
list = []

for i in string:
    if i < 'A':
        sum += int(i)
    else:
        list.append(i)
list.sort()
list.append(str(sum))
print("".join(list))

#K1KA5CB7