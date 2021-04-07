from prettytable import PrettyTable

x = PrettyTable()

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

    def get_allnodes(self,height,q):
        record=[]
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<=height):
                p=p.child
                level+=1
            record.append(p.data)
        x.add_row(record)          

    def get_nodes(self,heightoftree,attributes,q,selectedattributes):
       for a in q:
           if a.data in attributes:
               selectedattributes.append(a)

 
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.data))

        if self.children:
            for children in self.children:
                children.print_tree()
        if self.child:
            self.child.print_tree()

    def get_allnodeswithcon(self,k,q,conattribute,convalue,condition,selectedrecord):
        level=1
        length = len(q)
        for a in q:
                if a.data == conattribute:
                    e=a
        e=a
        e=e.child
        if (condition =='>'):
            while (level<k):
                if e.data > convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1
        elif(condition =='>='):
            while (level<k):
                if e.data >= convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1
        elif(condition =='<'):
            while (level<k):
                if e.data < convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1
        elif(condition =='<='):
            while (level<k):
                if e.data <= convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1
        elif(condition =='!='):
            while (level<k):
                if e.data != convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1
        elif(condition =='='):
            while (level<k):
                if e.data == convalue:
                    selectedrecord.append(level)
                    e=e.child
                    level+=1
                else:
                    e=e.child
                    level+=1


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


def select_operation(saved,attributes,condition,conattributes,convalues):
    width=saved[0]
    heightoftree=saved[1]
    root = TreeNode(saved[2])

    for i in range(3,width+3):
        root.add_children(TreeNode(saved[i]))

    for a in root.children:
        index=root.children.index(a)
        interval=index+width+3
        a.add_child(TreeNode(saved[interval]))
        temp=a.child
        n=width
        while(interval+n<len(saved)):
            b=saved[interval+n]
            temp.add_child(TreeNode(b))
            temp=temp.child
            n+=width

    q=root.children
    tableattribute=[]
    for i in range(width):
            a=q[i]
            tableattribute.append(a.data)

    if not attributes:
        if not conattributes:
            x.field_names = tableattribute
            for i in range(1,heightoftree):
                root.get_allnodes(i,q)
            print(x)
            x.clear_rows()
        else:
            selectedrecord=[]
            x.field_names = tableattribute
            root.get_allnodeswithcon(heightoftree,q,conattributes,convalues,condition,selectedrecord)
            for b in selectedrecord:
                root.get_allnodes(b,q)
            print(x)
            x.clear_rows()
                
    else:
        if not conattributes:
            selectedattributes=[]
            root.get_nodes(heightoftree,attributes,q,selectedattributes)
            x.field_names = attributes
            for i in range(1,heightoftree):
                root.get_allnodes(i,selectedattributes)
            print(x)
            x.clear_rows()
            
        else:
            selectedrecord=[]
            root.get_allnodeswithcon(heightoftree,q,conattributes,convalues,condition,selectedrecord)
            x.field_names = attributes
            for b in selectedrecord:
                selectedattributes=[]
                root.get_nodes(b,attributes,q,selectedattributes)
            for i in selectedrecord:
                root.get_allnodes(i,selectedattributes)
            print(x)
            x.clear_rows()




if __name__ == '__main__':

    attributes =['Name','Grade']
    condition='='
    conattributes='Contact'
    convalues=54556
    saved = [4, 5,'Student', 'StudentID', 'Name', 'Grade', 'Contact', '123', 'Piyush', 'ABC', 23546, '234', 'Nirmal', 'ACB', 54556, '345', 'Falgun', 'ACA', 74656, '476', 'Test', 'dfb', 23546]
    select_operation(saved,attributes,condition,conattributes,convalues)