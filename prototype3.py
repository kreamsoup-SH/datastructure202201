class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.prev = []
        self.next = []
        self.trsf = []
    def printnode(self):
        print("\"{}({})\"".format(self.name,self.line),end='\t')
        print("prev=[",end='')
        for j, prev in enumerate(self.prev):
            print("\"{}({})\"".format(prev.name,prev.line),end='')
        print("], next=[",end='')
        for j, next in enumerate(self.next):
            print("\"{}({})\"".format(next.name,next.line),end='')
        print("], trsf=[",end='')
        for j, trsf in enumerate(self.trsf):
            print("\"{}({})\"".format(trsf.name,trsf.line),end='')
        print("]")
        
def search_station(searchname, searchline=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if searchline!=None and searchline>0 and searchline<=len(NodeList):
        for _, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                # station.printnode()
                # print("searchname{},{}/".format(type(searchname),searchname))
                # print("stationame{},{}/".format(type(station.name),station.name))
                # print("searchline{},{}/".format(type(searchline),searchline))
                # print("stationlin{},{}/".format(type(station.line),station.line))
                # print(station.name == searchname)
                # print(station.line == searchline)
                if (station.name == searchname) and (station.line == searchline):
                    # print("!!!!!!!!!!")
                    return station
    else:
        # print("NodeList={}".format(NodeList))
        for i, Stations in enumerate(NodeList):
            # print("i={}, Stations=  {}".format(i, Stations))
            # print("search from line#{}".format(i+1))
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False


################ StationList Initialization ################
# filename="./stations_Done_data_processing.txt"
filename="./station_minimal.txt"
def getlinelist():
    f=open(filename,"r",encoding="UTF-8")
    rdline = f.readline().strip()
    stationline=0
    while rdline != '':
        # print("rdline:\"{}\"".format(rdline))
        stations = rdline.split(",")
        print("{}".format(stations))
        # print("stations={}".format(stations))
        if stations[0].isnumeric():
            # print("stations[0].isnumeric()")
            stationline = int(stations[0])
            while len(NodeList)<stationline:
                NodeList.append([])
            # print("stationline=",stationline)
            # print(NodeList)
        else:
            for i, stationname in enumerate(stations):
                found = search_station(stationname,stationline)
                # print("i={}".format(i))
                # if(found!=False):
                #     print("found={}({})".format(found.name, found.line))
                # else:
                #     print("found={}".format(found))

                # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
                if found == False:  # new station in current line
                    if(i<=0):       # 분기점 or 시작점
                        newnode = StationNode(stationname, stationline)

                        ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                        trsffound = search_station(stationname)
                        if trsffound != False:
                            newnode.trsf.append(trsffound)
                            trsffound.trsf.append(newnode)
                        ###################################################

                        NodeList[stationline-1].append(newnode)
                    elif(i>0):      # 그냥 중간역
                        newnode = StationNode(stationname, stationline)

                        ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                        for checkline in range(1,5):
                            trsffound = search_station(stationname,checkline)
                            if trsffound != False:
                                newnode.trsf.append(trsffound)
                                trsffound.trsf.append(newnode)
                        ###################################################

                        prevstation = search_station(stations[i-1], stationline)
                        prevstation.next.append(newnode)
                        newnode.prev.append(prevstation)
                        NodeList[stationline-1].append(newnode)
                
        # print("-------------------------------------------")
        # for i,NodeLine in enumerate(NodeList):
        #     for j, Node in enumerate(NodeLine):
        #         Node.printnode()
        # print("-------------------------------------------")
        # input()
        rdline = f.readline().strip()
    f.close()
############################################################

NodeList=[]
getlinelist()
sicheong = search_station("시청",2)
chungjeongro = search_station("충정로",2)
sicheong.prev.append(chungjeongro)
chungjeongro.next.append(sicheong)


############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.

# search_result = search_station("방화")
for i,NodeLine in enumerate(NodeList):
    for j, Node in enumerate(NodeLine):
        Node.printnode()