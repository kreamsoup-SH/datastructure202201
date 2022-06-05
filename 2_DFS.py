import pandas as pd

#파일 전처리(이상한 부분 삭제)
filename = './edges.csv'
rawData = pd.read_csv(filename,encoding='UTF-8')
file =  rawData

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
        if len(self.prev)!= 0:
            prev = self.prev[0]
            print("\"{}({}) : {}\"".format(prev.name,prev.line, self.prev[1]),end='')
        print("], next=[",end='')
        for j in range(len(self.next)):
            next = self.next[j]
            next2 = next[0]
            print("\"{}({}) : {}\"".format(next2.name,next2.line,next[1] ),end='')
        print("], trsf=[",end='')
        for j in range(len(self.trsf)):
            trsf = self.trsf[j]
            trsf1 = trsf[0]
            print("\"{}({}) : {}\"".format(trsf1.name,trsf1.line, trsf[1]),end='')
        print("]")

def append_next(self):
    self.next.append([])
    return len(self.next)-1

def append_trsf(self):
    self.trsf.append([])
    return len(self.trsf)-1
        
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
    else:  #찾고자 하는 특정 호선이 존재 안 함.
        # print("NodeList={}".format(NodeList))
        for i, Stations in enumerate(NodeList):
            # print("i={}, Stations=  {}".format(i, Stations))
            # print("search from line#{}".format(i+1))
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False


################ StationList Initialization ################

def getlinelist():
    #Data로 file 사용
    for (idx, row) in (file.iterrows()):
        time = row[2]
        stationname = row[1]
        stationline = row[0]
        # print("rdline:\"{}\"".format(rdline))
        #print("{}".format(stationname))
        # print("stations={}".format(stations))
        while len(NodeList)<stationline:
            NodeList.append([])
        # print("stationline=",stationline)
            # print(NodeList)
        found = search_station(stationname,stationline)
                # print("i={}".format(i))
                # if(found!=False):
                #     print("found={}({})".format(found.name, found.line))
                # else:
                #     print("found={}".format(found))

                # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
        if found == False:  # new station in current line
            if(stationline != file.iloc[idx-1,0]):       #시작점 (호선이 달라지는 경우)
                newnode = StationNode(stationname, stationline)
                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                trsffound = search_station(stationname)
                if trsffound != False:
                    edge = 3
                    i = append_trsf(newnode)
                    j = append_trsf(trsffound)
                    newnode.trsf[i].append(trsffound)
                    trsffound.trsf[j].append(newnode)
                    newnode.trsf[i].append(edge)
                    trsffound.trsf[j].append(edge)
                    #print(newnode.trsf)
                    #print(trsffound.trsf)
           ###################################################
                print(newnode.name, newnode.next, newnode.trsf)
                NodeList[stationline-1].append(newnode)

            else:      # 그냥 중간역
                newnode = StationNode(stationname, stationline)
                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                for checkline in range(1,5):
                    trsffound = search_station(stationname,checkline)
                    if trsffound != False:
                        edge = 3
                        i = append_trsf(newnode)
                        j = append_trsf(trsffound)
                        newnode.trsf[i].append(trsffound)
                        trsffound.trsf[j].append(newnode)
                        newnode.trsf[i].append(edge)
                        trsffound.trsf[j].append(edge)
                        #print(newnode.trsf)
                        #print(trsffound.trsf)
                        ###################################################

                prevstation = search_station(file.iloc[idx-1,1],file.iloc[idx-1,0])
                i = append_next(prevstation)
                prevstation.next[i].append(newnode)
                newnode.prev.append(prevstation)
                prevstation.next[i].append(time)
                newnode.prev.append(time)
                prev = newnode.prev[0]

                NodeList[stationline-1].append(newnode)
       
        # print("-------------------------------------------")
        # for i,NodeLine in enumerate(NodeList):
        #     for j, Node in enumerate(NodeLine):
        #         Node.printnode()
        # print("-------------------------------------------")
        # input()
############################################################


NodeList = []
getlinelist()
#sicheong = search_station("시청",2)
#chungjeongro = search_station("충정로",2)
#sicheong.prev.append(chungjeongro)
#chungjeongro.next.append(sicheong)


############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.

# search_result = search_station("방화")
for i,NodeLine in enumerate(NodeList):
    for j, Node in enumerate(NodeLine):
        Node.printnode()

