f=open("./stations.txt","r",encoding="UTF-8")

# lines = f.readlines()

# StationList=[]

# for i, line in enumerate(lines):
#     print("{}호선".format(i+1))
#     stations = line.split(",")
#     for j, station in enumerate(stations):
#         print(station,end=" - ")

#         if not j%5 and j!=0:
#             print()

# print("--------------------")
# print(StationList)

line = f.readline().strip()
StationList=[]
while line != '':
    stations = line.split(",")
    StationList.append(stations)
    line = f.readline().strip()


print(StationList)
f.close()