class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,d):
        new_node=Node(d)
        if self.front is None:
            self.front=self.rear=new_node
        else:
            self.rear.ref=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front==self.rear:
            de=self.front.data
            self.front=self.rear=None
        else:
            de=self.front.data
            self.front=self.front.ref
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data)
q=int(input())
que=Queue()
for i in range(q):
    s=input()
    s=s.split()
    if s[0]=="1":
        que.enqueue(s[1])
    elif s[0]=="2":
        que.dequeue()
    elif s[0]=="3":
        que.display()
