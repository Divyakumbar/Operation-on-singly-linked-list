class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Data doesn't found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("element not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_to_emptyll(self,data):
            if self.head is None:
                new_node=Node(data)
                self.head=new_node
            else:
                print("Linked list is not empty")
    def delete_start(self):
        if self.head is None:
            print("Linked list is empty.You can't delete")
        else:
            self.head=self.head.ref
            print("Deleted")
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_end(50)
LL1.add_after(2,10)
LL1.add_after(3,50)
# LL1.add_after(4,70)
# LL1.add_before(2,30)
# LL1.add_to_emptyll(20)
# LL1.add_to_emptyll(30)
LL1.delete_start()
LL1.delete_end()
LL1.delete_end()

LL1.print_ll()