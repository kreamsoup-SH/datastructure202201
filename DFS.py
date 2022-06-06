import pandas as pd
from sqlalchemy import false

def StationDict(_station, _time):
    return {"station":_station, "time":_time}

class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.time = 10000000
        self.prev = []
        self.next = []
        self.trsf = []
        self.checked= false
    def printnode(self):
        print("\"{}({})\"".format(self.name,self.line),end='\t')
        print("prev=[ ",end='')
        for _,prev in enumerate(self.prev):
            print("({}({})-{}) ".format(prev["station"].name, prev["station"].line, int(prev["time"])),end='')
        print("], next=[ ",end='')
        for _,next in enumerate(self.next):
            print("({}({})-{}) ".format(next["station"].name, next["station"].line, int(next["time"])),end='')
        print("], trsf=[ ",end='')
        for _,trsf in enumerate(self.trsf):
            print("({}({})-{}) ".format(trsf["station"].name, trsf["station"].line, int(trsf["time"])),end='')
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
    for checkline in range(1,newnode.line):
        trsffound = search_station(searchname, checkline)
        if trsffound:
            edge = 180
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
filename = './edges_sec.csv'
file = pd.read_csv(filename,encoding='UTF-8')

# 맵 생성
NodeList = []
getlinelist()
## 2호선 예외항목 -> 뚝섬(2), 성수(2) 연결하기
DS = search_station("뚝섬",2)
SS = search_station("성수",2)
time=90
DS.append_prev(SS,time)
SS.append_next(DS,time)

# search_result = search_station("방화")
# for i,NodeLine in enumerate(NodeList):
#     for j, Node in enumerate(NodeLine):
#         Node.printnode()

#################################################################################


def find_route(_start : str, _end : str):
    start   = search_station(_start)
    end     = search_station(_end  )
    if(start==false or end==false):
        print("정확한 역명을 입력해주세요.")
        return false

    DFS(start,end)

#################################################################################

dirlist=[]
def DFS(start : StationNode):
    dir=[]
    dir.append(start)
    if dir


# def DFS(current : StationNode, end : StationNode, dir=[], fromnode=StationNode("None",0)):
#     print ("\n\ncurrent:{}({}), from:{}({}) -- START\n".format(current.name,current.line, fromnode.name, fromnode.line))
#     # 현재역이 도착지인지 확인
#     if current.name == end.name:
#         print("end!!!! {}, {}".format(current.name, end.name))
#         i=0
#         while(dir[i].name==dir[i+1].name):
#             i+=1
#         print("{}->".format(dir[i].name))
#         time=0
#         for station in dir[i:]:
#             print("{}->".format(station.name),end='')
#             time+=station.time
#         print("도착.\n소요시간={}분{}초".format(time//60,time%60))
#         dirlist.append([dir,time])
#         return
#     # 이미 왔던 역인지 확인
#     for node in dir:
#         if node == current:
#             print("already?!!!! {}, {}".format(node.name, current.name))
#             return current
    
#     # 현재역을 경로에 추가
#     dir.append(current)

#     # 현재역과 이어져있는 역으로 이동

#     for stationdict in current.next:
#         print("{}({}) for next".format(current.name,current.line))
#         for node in dir:
#             print("{}-".format(node.name),end='')

#         print("DFS({},{},{},{})".format(stationdict["station"].name,end.name,"dir",current.name))
#         if (stationdict["station"] == fromnode):
#             print("이미 여기서 온거임")
#             return current
#         DFS(stationdict["station"], end, dir, current)
#         dir.pop()
#     for stationdict in current.trsf:
#         print("{}({}) for trsf".format(current.name,current.line))
#         for node in dir:
#             print("{}-".format(node.name),end='')
#         if (stationdict["station"] == fromnode):
#             print("이미 여기서 온거임")
#             return current
#         DFS(stationdict["station"], end, dir, current)
#         dir.pop()
#     for stationdict in current.prev:
#         print("{}({}) for prev".format(current.name,current.line))
#         for node in dir:
#             print("{}-".format(node.name),end='')
#         if (stationdict["station"] == fromnode):
#             print("이미 여기서 온거임")
#             return current
#         DFS(stationdict["station"], end, dir, current)
#         dir.pop()
    
#     print ("current:{}({}) -- END\n".format(current.name,current.line))
#     return current

find_route("성수", "용산")
print(dirlist)