class StationNode:
    def __init__(self, data):
        self.data = data
        self.prev = []
        self.next = []

class DLinkedList():
    def __init__(self, station,transf_to=None):
        self.head = StationNode(station)
        self.tail = self.head
        if(transf_to!=None):
            self.next=transf_to     # transf_to = line number

    def push(self, station):
        if self.head == None:
            self.head = StationNode(station)
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            insertnode = StationNode(station,prev=current)
            current.next = insertnode
            self.tail = insertnode
    
    def pop(self):
        current = self.head
        last = self.head.next
        while last.next != None:
            current = current.next
            last = last.next
        last=None
        current.next=None

    def printlist(self):
        current = self.head
        while current != None:
            print("{}".format(current.data))
            current = current.next

def search_station(line,name):
    # Search specific station in {StationList}
    # while loop on {StationList}, check if {StationList[i].name} is {"name"}
    # If station we want is found then now {target} is {StationList[i]}
    target=None
    return target


line1 = DLinkedList(1111)
line1.push(10)
line1.push([20,25])
line1.push(40)
line1.push(30)
line1.push(60)
line1.push(50)

line1.printlist()

print("---------")
line1.pop()
line1.printlist()

print("---------")
line1.pop()
line1.printlist()