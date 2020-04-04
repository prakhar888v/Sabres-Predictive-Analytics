import csv

path = 'C:\\Users\\prakh\\OneDrive\\Documents\\Sabres project\\Buffalo Sabres data\\Sabres home games.csv'
path1 = 'C:\\Users\\prakh\\OneDrive\\Documents\\Sabres project\\Buffalo Sabres data\\Sabres home games1.csv'

with open(path,'r') as f:
    reader = csv.reader(f)
    l = list(reader)

for i in range(1,len(l)):
    temp_list = l[i][10].split(',')
    l[i][11] = int(''.join(temp_list))

with open(path,'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)




