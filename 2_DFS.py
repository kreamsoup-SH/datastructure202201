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

    def append_next(self,nextstation):
        self.next.append([])

    def append_trsf(self,trsfstation):
        self.trsf.append([])

def search_station(searchname, searchline=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if searchline!=None and searchline>0 and searchline<=len(NodeList):
        for _, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                if (station.name == searchname) and (station.line == searchline):
                    return station
    else:  #찾고자 하는 특정 호선이 존재 안 함.
        for i, Stations in enumerate(NodeList):
            for j, station in enumerate(Stations):
                if station.name == searchname:
                    return station
    return False


################ StationList Initialization ################

def getlinelist():
    #Data로 file 사용
    for (idx, row) in (file.iterrows()):
        stationline = row[0]
        stationname = row[1]
        time = row[2]
        while len(NodeList)<stationline:
            NodeList.append([])
        found = search_station(stationname,stationline)
        
        # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
        if found == False:  # new station in current line
            if(stationline != file.iloc[idx-1,0]):       #시작점 (호선이 달라지는 경우)
                newnode = StationNode(stationname, stationline)
                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에 추가##
                trsffound = search_station(stationname)
                if trsffound != False:
                    edge = 3
                    newnode.append_trsf()
                    trsffound.append_trsf()
                    newnode.trsf[i].append(trsffound)
                    trsffound.trsf[j].append(newnode)
                    newnode.trsf[i].append(edge)
                    trsffound.trsf[j].append(edge)
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
                ###################################################

                prevstation = search_station(file.iloc[idx-1,1],file.iloc[idx-1,0])
                i = append_next(prevstation)
                prevstation.next[i].append(newnode)
                newnode.prev.append(prevstation)
                prevstation.next[i].append(time)
                newnode.prev.append(time)
                prev = newnode.prev[0]

                NodeList[stationline-1].append(newnode)
                
############################################################
## 뚝섬(2), 성수(2) 연결하기

NodeList = []
getlinelist()
# DS = search_station("뚝섬",2)
# SS = search_station("성수",2)
# DS.prev.append(SS)
# SS.next.append(DS)


############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.

# search_result = search_station("방화")
for i,NodeLine in enumerate(NodeList):
    for j, Node in enumerate(NodeLine):
        Node.printnode()

