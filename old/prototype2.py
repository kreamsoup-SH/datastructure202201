class StationNode:
    def __init__(self, data):
        self.data = data
        self.prev = []
        self.next = []
    def __str__(self):
        print("{}, prev={}, next={}".format(self.data, self.prev, self.next))
        return self.data["name"]
    def printnode(self):
        print("\"{}\"".format(self.data["name"]),end=' ')
        print("prev=[",end='')
        for j, prev in enumerate(self.prev):
            print("\"{}\"".format(prev.data["name"]),end='')
        print("], next=[",end='')
        for j, next in enumerate(self.next):
            print("\"{}\"".format(next.data["name"]),end='')
        print("]")
        
def search_station(searchname, line=None):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    
    if line!=None:
        for _, station in enumerate(NodeList[line-1]):
            if station.data["name"] is searchname:
                return station
    else:
        for i, Stations in enumerate(NodeList):
            print("line#{}".format(i+1))
            for _, station in enumerate(Stations):
                # print(station.data["name"],end=' ')
                # print("?=? ",end='')
                # print(searchname)
                if station.data["name"] == searchname:
                    # print("found!")
                    return station
    return StationNode({"name":"NotFound"})


################ StationList Initialization ################
def getlinelist():
    f=open("./stations.txt","r",encoding="UTF-8")
    line = f.readline().strip()
    while line != '':
        stations = line.split(",")
        StationList.append(stations)
        line = f.readline().strip()
    # print(StationList)
    f.close()

StationList=[]
getlinelist()
NodeList=[]
for n, Stations in enumerate(StationList):
    print("StationList[{}] = {}".format(n,Stations),end="\n\n")
    NodeList.append([])
    for i, station in enumerate(Stations):
        newnode = StationNode({"name":station})
        NodeList[n].append(newnode)
        if i>0:
            NodeList[n][i-1].next.append(newnode)
            newnode.prev.append(NodeList[n][i-1])
    # print(NodeList)
    for i, node in enumerate(NodeList[n]):
        node.printnode()
    print("StationList[{}] has been printed!\n-------------------".format(n))
############################################################

############ search_station ############
## let's try testing search function! change "을지로" to another station name.
## Because "을지로" doesn't exist, {search_result} shows name "NotFound".
## If you change it to existing name, then you can get right result.
search_result = search_station("을지로")
search_result.printnode()