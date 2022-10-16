class node:

    def __init__(self,value=None):
        self.value=value
        self.next=None

class linked_list:
    
    def __init__(self):
        self.head=node()
    
    def append(self , new_node):
        current=self.head
        while current.next:
            current=current.next
        current.next=node(new_node)
    
    def length(self):
        total=0
        current=self.head
        while current.next:
            current=current.next
            total+=1
        print(f'Length = {total}')
    
    def display(self):
        l=[]
        current=self.head
        while current.next:
            current=current.next
            l.append(current.value)
        print(l)
    
    def get(self,position):
        current = self.head
        index = 0
        while current.next:
            current = current.next
            if index == position:
                print(f"Node #{position+1} is {current.value}")
            index+=1
        return

    
    def remove(self,position):
        current=self.head
        index=0
        while current.next:
            last_node=current
            current=current.next
            if index==position:
                last_node.next=current.next
            index+=1
        return

    def insert(self,new_node,position):
        current=self.head
        new_node=node(new_node)
        index=0
        while current.next:
            last_node = current
            current = current.next
            if index == position:
                last_node.next = new_node
                new_node.next = current
            index += 1 
        return        
    
    def replace(self,old_node,new_node):
        current = self.head
        new_node=node(new_node)
        while current.next:
            last_node=current
            current=current.next
            if current.value == old_node:
                current.value = new_node.value
        return            





ll=linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(6)
ll.length()
ll.display()
ll.remove(2)
ll.display()
ll.insert(3,2)
ll.display()
ll.insert(0,0)
ll.display()
ll.replace(6,5)
ll.display()


