data_list =[]
data_list2 =[]
with open('data.txt') as f:
    for line in f.readlines():
        data_list.append(line)

for item in data_list:
    data_list2.append(float(item.replace('\n', '').replace(',', '.')))

print(len(data_list2))