class StationNode:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.prev = []
        self.next = []
        self.trsf = []

### 4개의 역 ###
신도림1 = StationNode("신도림", "1")
구로1 = StationNode("구로", "1")
구일1 = StationNode("구일", "1")
가산디지털단지1 = StationNode("가산디지털단지", "1")
신도림2 = StationNode("신도림", "2")
문래2 = StationNode("문래", "2")

### 각 역별 데이터 ###
신도림1.next    = [{"station" : 구로1, "time":"1:30"}]
신도림1.prev    = []
신도림1.trsf    = [{"station" : 신도림2, "time":"3:00"}]

구로1.next      = [{"station" : 구일1, "time":"1:30"},{"station" : 가산디지털단지1, "time":"2:00"}]
구로1.prev      = [{"station" : 신도림1, "time":"1:30"}]
구로1.trsf      = []

구일1.next      = []
구일1.prev      = [{"station" : 구로1, "time":"1:30"}]
구일1.trsf      = []
