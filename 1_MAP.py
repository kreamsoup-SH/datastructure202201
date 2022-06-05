import pandas as pd


def StationDict(_station, _time):
    return {"station":_station, "time":_time}

class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.prev = []
        self.next = []
        self.trsf = []
    def printnode(self):
        print("\"{}({})\"".format(self.name,self.line),end='\t')
        print("prev=[ ",end='')
        for _,prev in enumerate(self.prev):
            print("({}({})-{}) ".format(prev["station"].name, prev["station"].line, prev["time"]),end='')
        print("], next=[ ",end='')
        for _,next in enumerate(self.next):
            print("({}({})-{}) ".format(next["station"].name, next["station"].line, next["time"]),end='')
        print("], trsf=[ ",end='')
        for _,trsf in enumerate(self.trsf):
            print("({}({})-{}) ".format(trsf["station"].name, trsf["station"].line, trsf["time"]),end='')
        print("]")

    def append_prev(self,prevstation,time):
        self.prev.append(StationDict(prevstation,time))
    def append_next(self,nextstation,time):
        self.next.append(StationDict(nextstation,time))
    def append_trsf(self,trsfstation,time):
        self.trsf.append(StationDict(trsfstation,time))

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

def check_trsf(newnode, searchname):
    for checkline in range(1,5):
        trsffound = search_station(searchname, checkline)
        if trsffound:
            edge = "3:00"
            newnode.append_trsf(trsffound, edge)
            trsffound.append_trsf(newnode, edge)

################ StationList Initialization ################

def getlinelist():
    #Data로 file 사용
    prev=StationNode("None","0")
    for (idx, row) in (file.iterrows()):
        stationline = row[0]
        stationname = row[1]
        time = row[2]
        
        while len(NodeList)<stationline:
            NodeList.append([])
        
        found = search_station(stationname,stationline)
        # 만약 새로운역이면 추가. 이미 존재하는역(현재 라인 내에서 한정)일경우 패스
        if found == False:  # new station in current line

            ##########################
            ##  본격적인 데이터 입력 코드 ##
            ##########################
            newnode = StationNode(stationname, stationline)
            if(stationline != prev.line):
                #시작점 (호선이 달라지는 경우)

                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에추가
                check_trsf(newnode, stationname)
                #NodeList에 새로운 노드 추가
                NodeList[stationline-1].append(newnode)
                prev = newnode
                
            else:
                #그냥 중간역

                ##환승역 체크. 다른노선에 동일명의 역이 존재할경우 trsf에추가
                check_trsf(newnode,stationname)
                ##이전역과 현재역을 연결
                prev.append_next(newnode, time)
                # "이전역에서오는시간=이전역으로가는시간"으로 가정하면
                newnode.append_prev(prev, time)
                #NodeList에 새로운 노드 추가
                NodeList[stationline-1].append(newnode)
                prev=newnode
        else:
            prev = found

                
############################################################
# 파일 전처리
filename = './edges.csv'
file = pd.read_csv(filename,encoding='UTF-8')

# 맵 생성
NodeList = []
getlinelist()
## 2호선 예외항목 -> 뚝섬(2), 성수(2) 연결하기
DS = search_station("뚝섬",2)
SS = search_station("성수",2)
time="1:30"
DS.append_prev(SS,time)
SS.append_next(DS,time)

# search_result = search_station("방화")
for i,NodeLine in enumerate(NodeList):
    for j, Node in enumerate(NodeLine):
        Node.printnode()

