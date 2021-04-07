class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.child=None
        self.parent=None

    def add_children(self, children):
        children.parent = self
        self.children.append(children)

    def add_child(self,child):
        child.parent = self
        self.child = child

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_allnodes(self,k,q):
        j=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<=k):
                p=p.child
                level+=1
            j.append(p.data)
        print(j)

    def get_nodes(self,k,attributes):
       q=[]
       for a in root.children:
           if a.data in attributes:
               q.append(a)
       root.get_allnodes(k,q)

 
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.data))

        if self.children:
            for children in self.children:
                children.print_tree()
        if self.child:
            self.child.print_tree()

    def get_allnodeswithcon(self,k,q,conattribute,convalue):
        j=[]
        level=1
        length = len(q)
        for a in root.children:
                if a.data == conattribute:
                    c= root.children.index(a)
        e=q[c]
        e=e.child
        while (level<k):
            if e.data > convalue:
                j.append(level)
                e=e.child
                level+=1
            else:
                e=e.child
                level+=1
        for b in j:
            root.get_allnodes(b,q)

    def get_nodeswithcon(self,k,q,conattribute,convalue,attributes):
        j=[]
        level=1
        length = len(q)
        for a in root.children:
                if a.data == conattribute:
                    c= root.children.index(a)
        e=q[c]
        e=e.child
        while (level<k):
            if e.data > convalue:
                j.append(level)
                e=e.child
                level+=1
            else:
                e=e.child
                level+=1
        for b in j:
            root.get_nodes(b,attributes)

    def delete_connodes(self,k,q,conattribute,convalue):
        j=[]
        level=1
        length = len(q)
        for a in root.children:
                if a.data == conattribute:
                    c= root.children.index(a)
        e=q[c]
        e=e.child
        while (level<k):
            if e.data == convalue:
                j.append(level)
                e=e.child
                level+=1
            else:
                e=e.child
                level+=1
        for b in j:
            root.delete_nodes(b,attributes)

    def delete_nodes(self,k,attributes):
        j=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<k-1):
                p=p.child
                level+=1
            p.child=p.child.child

    def delete_allnodes(self,q):
        for a in q:
            a.child=None


def build_tree():
    root = TreeNode("Student")

    Id = TreeNode("StudentID")
    id1 = TreeNode("123")
    id2 = TreeNode("234")
    id3 = TreeNode("345")
    id4 = TreeNode("476")

    Name = TreeNode("Name")
    n1 = TreeNode("Piyush")
    n2 = TreeNode("Nirmal")
    n3 = TreeNode("Falgun")
    n4 = TreeNode("Test")

    Grade = TreeNode("Grade")
    g1 = TreeNode("ABC")
    g2 = TreeNode("ACB")
    g3 = TreeNode("ACA")
    g4 = TreeNode("dfb")

    Contact = TreeNode("Contact")
    c1 = TreeNode(23546)
    c2 = TreeNode(54556)
    c3 = TreeNode(74656)
    c4 = TreeNode(233546)


    root.add_children(Id)
    root.add_children(Name)
    root.add_children(Grade)
    root.add_children(Contact)
    Id.add_child(id1)
    id1.add_child(id2)
    id2.add_child(id3)
    id3.add_child(id4)
    Name.add_child(n1)
    n1.add_child(n2)
    n2.add_child(n3)
    n3.add_child(n4)
    Grade.add_child(g1)
    g1.add_child(g2)
    g2.add_child(g3)
    g3.add_child(g4)
    Contact.add_child(c1)
    c1.add_child(c2)
    c2.add_child(c3)
    c3.add_child(c4)
    return root

if __name__ == '__main__':
    root = build_tree()

    q=root.children
    attributes=["Name","Contact"]
    conatribute="Contact"
    convalue=23546

    #print("Tree:")
    #root.print_tree()

    #print("Select * from Student")
    #for i in range (1,5):
       # root.get_allnodes(i,q)

    #print("Select Name , Contact from Student")
    #for i in range (1,5):
        #root.get_nodes(i,attributes)

    #print("Select * from Student where Contact > 23546")
    #root.get_allnodeswithcon(5,q,conatribute,convalue)

    #print("Select Name, Contact from Student where Contact > 23546")
    #root.get_nodeswithcon(5,q,conatribute,convalue,attributes)

    print("Select * from Student")
    for i in range (1,5):
       root.get_allnodes(i,q)

    print("Delete from student where Contact = 23546")
    root.delete_connodes(5,q,conatribute,convalue)

    print("Select * from Student")
    for i in range (1,4):
       root.get_allnodes(i,q)

    print("Delete from student")
    root.delete_allnodes(q)
    root.print_tree()