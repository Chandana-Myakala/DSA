''' we dont use binary search in linked list because of indexing.we dont have index in LL'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t = self.head
        while t!=None:
            print(t.data, end='->')
            t = t.next
        print('None')
    def sum_all(self):
        t=self.head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.next
        print(s)
    def sum_all_even(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
    def sum_even_pos(self):
        t=self.head
        s=0
        pos=1
        while t!=None:
            if pos%2==0:
                s=s+t.data
            t=t.next
            pos+=1
        print("Sum of elements at even positions:",s)
    def sec_largest(self):
        t=self.head
        m1=m2=None
        while t!=None:
            if m1==None or t.data>m1.data:
                if m1==None or t.data!=m1.data:
                    m2=m1
                m1=t
            elif t.data!=m1.data and (m2==None or t.data>m2.data):
                m2=t
            t=t.next
        if m2:
            print(m2.data)
    def count_pair(self,k): #consecutive pair sum where sum<=k
        t=self.head
        c=0
        while t.next!=None:
            if t.data+t.next.data<=k:
                c=c+1
            t=t.next
        print(c)
    def count_all_pair(self, k): #all possible pairs
        t=self.head
        c=0
        while t.next!=None:
            t1=t.next
            while t1!=None:
                if t.data+t1.data<=k:
                    c+=1
                t1=t1.next
            t=t.next
        print(c)
    #print the sechalf of the LL.linked list must be in even length
    def sec_half_ofLL(self):
        t=self.head
        c=0
        while t:
            c+=1
            t=t.next
        mid=c//2
        t=self.head
        for _ in range(mid):
            t=t.next
        while t:
            print(t.data,end='->')
            t=t.next
        print("None")
    def mid(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            s=s.next
        print(s.data)
    def first_half(self):
        f=self.head
        s=self.head
        prev=None
        while f and f.next:
            f=f.next.next
            prev=s
            s=s.next
        t=self.head
        while t != s:
            print(t.data, end='->')
            t = t.next
        print("None")
    #print the kth node from the last
    def kth_from_end(self, k):
        f=self.head
        s=self.head
        for _ in range(k):
            if(f!=None):
                f=f.next
        while f!=None:
            f=f.next
            s=s.next
        if s!=None:
            print(s.data)
    def kth_del(self,k):
        f=self.head
        for i in range(k):
            if(f!=None):
                f=f.next
        if f!=None:
            self.head=self.head.next
            return
        s=self.head
        prev=None
        while(f!=None):
            prev=s
            s=s.next
            f=f.next
        if prev!=None and s!=None:
            prev.next=s.next
    #swap the nodes if it is even,if it is odd leave the last node same
    def swap_nodes(self):
        t=self.head
        while t!=None and t.next!=None:
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
    #bubble sort
    def bubblesort(self):
        if self.head==None:
            return
        f=True
        while f:
            f=False
            t=self.head
            while t.next!=None:
                if t.data>t.next.data:
                    t.data,t.next.data=t.next.data,t.data
                    f=True
                t=t.next
    def kth_largest(self,k):
        temp=self.head
        k1=k
        while temp!=None:
            f=0
            t=self.head
            while t.next!=None:
                if t.data>t.next.data:
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
            if f==0:
                break
            temp=temp.next
            k-=1
        self.kth_from_end(k1)
    def check_loop(self):
        f=self.head
        s=self.head
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
            if f==s:
                print('loop')
                return
        print('no loop')
l1=Linkedlist()
l1.head=node(5)
l1.add_back(2)
l1.add_back(4)
l1.add_back(7)
l1.add_back(3)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)
l1.display()
l1.sum_all()
l1.sum_all_even()
l1.sum_even_pos()
l1.sec_largest()
l1.count_pair(10)
l1.count_all_pair(10)
l1.sec_half_ofLL()
l1.mid()
l1.first_half()
l1.kth_from_end(3)
l1.kth_del(3)
l1.display()
l1.swap_nodes()
l1.display()
l1.bubblesort()
l1.display()
l1.kth_largest(2)
l1.check_loop()
l2=Linkedlist()
l2.head=node(100)
l2.head.next=node(200)
l2.head.next.next=node(300)
l2.head.next.next.next=node(400)
l2.head.next.next.next.next=node(500)
l2.display()
l2.check_loop()