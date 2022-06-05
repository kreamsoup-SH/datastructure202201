import pandas as pd
filename = './edges.csv'
file = pd.read_csv(filename,encoding='UTF-8') 

output = open("edges_sec.csv",'w',encoding='utf-8')
output.write("호선,역,시간(sec)\n")
for (idx, row) in (file.iterrows()):
    if type(row[2])==str:
        time = row[2].split(':')
        sec = int(time[0])*60 + int(time[1])
        # print(sec)
        output.write("{},{},{}\n".format(row[0],row[1],sec))
    else:
        output.write("{},{},\n".format(row[0],row[1]))