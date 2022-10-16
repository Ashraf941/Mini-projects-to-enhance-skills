class Element:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=Element()
    
    def append(self,value):
        new_element=Element(value)
        current=self.head
        while current.next != None:
            current=current.next
        current.next=new_element
    
    def length(self):
        total=0
        current=self.head
        while current.next != None:
            current=current.next
            total+=1
        return total    
    
    def display(self):
        l=[]
        current=self.head
        while current.next != None:
            current=current.next
            l.append(current.data)
        print(l)

    def get(self,index):
        current=self.head
        currentindex=0
        while True:
            current=current.next
            if currentindex == index:
                return current.data
            currentindex+=1
    
    def insert(self,newdata,position):
        current=self.head
        index=0
        while current.next:
            current=current.next
            temp=current.next
            if index == position-1:
                current.next = Element(newdata)
                current.next.next = temp
            index+=1

    def delete(self,index):
        current=self.head
        currentindex=0
        while True:
            lastelement=current
            current=current.next
            if currentindex == index:
                lastelement.next=current.next
                return
            currentindex+=1
ll=LinkedList()
ll.display()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.display()
ll.insert(3,3)
ll.display()

    





