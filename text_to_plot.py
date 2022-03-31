from text_file_reading import read_with_split
import matplotlib.pyplot as plt

temp = read_with_split('test.txt','\n')
temp_int = []
days = []
i = 1


temp_int = []
for elem in temp:
    temp_int.append(int(elem))
    days.append(i)
    i+=1
plt.plot(days, temp_int)
plt.show()