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

    def get_nodeswithcon(self,k,q,conattribute,convalue,z):
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
            root.get_nodes(b,z)

    def update_nodes2(self,k,attributes,values):
        q=[]
        for a in root.children:
           if a.data in attributes:
               q.append(a)
        j=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<=k):
                p=p.child
                level+=1
            p.data=values[i]

    def update_nodes(self,k,attributes,values):
        q=[]
        for a in root.children:
           if a.data in attributes:
               q.append(a)
        root.update_allnodes(k,q,values)

    def update_allnodes(self,k,q,values):
        j=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<=k):
                p.data=values[i]
                p=p.child
                level+=1

    def update_connodes(self,k,q,attributes,values,conattribute,convalue):
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
            root.update_nodes2(b,attributes,values)


    def saved_tree(self):
        saved2=[]
        q=root.children
        saved2.append(len(q))
        saved2.append(root.data)
        while(len(q)!=0):
            z=q[0]
            if (z!=None):
                saved2.append(z.data)
                q.append(z.child)
                q.remove(z)
            else:
                break
        print(saved2)
 
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.data))

        if self.children:
            for children in self.children:
                children.print_tree()
        if self.child:
            self.child.print_tree()

    def insert_node(self,k,q,attributes,newvalues):
        j=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<=k):
                p=p.child
                level+=1
            p.add_child(TreeNode(newvalues[i]))


def create_tree(tablename,attributes):
    root =TreeNode(tablename)
    for a in attributes:
        root.add_children(TreeNode(a))
    root.print_tree()


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
    c4 = TreeNode(23546)


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
    values=["asz",236]
    conatribute="Contact"
    convalue=23546
    tablename = "User"
    newvalues=[276,"Test2","Grade2","Contact2"]

    #print("Create table User (Name  varchar(255), Contact int ) ")
    #create_tree(tablename,attributes)

    print("Select * from Student")
    for i in range (1,5):
        root.get_allnodes(i,q)

    #print("Update student set Name='asz',Contact=236")
    #root.update_nodes(5,attributes,values)

    #print("Update student set Name='asz',Contact=236 where Contact > 23546" )
    #root.update_connodes(5,q,attributes,values,conatribute,convalue)
    
    print("Insert into Student Values(276,'Test2','Grade2','Contact2')")
    root.insert_node(4,q,attributes,newvalues)

    print("Select * from Student")
    for i in range (1,6):
        root.get_allnodes(i,q)