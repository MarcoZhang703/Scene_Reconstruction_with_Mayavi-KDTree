file = open('n.txt', "r")
lines = []

for i in file:
    lines.append(i)

file.close()


new = []

for line in lines:
    new.append(line.replace(" ", ",", 3))

file_write_obj = open("n_new.txt", 'w')

for var in new:
    file_write_obj.writelines(var)
file_write_obj.close()


#下面的方法是用来删掉最后一个字符的

'''
new = []

for line in lines:
    new.append(line[0:30])

file_write_obj = open('000_new2.txt', 'w')
for var in new:
    file_write_obj.writelines(var)
    file_write_obj.writelines('\n')
file_write_obj.close()
'''