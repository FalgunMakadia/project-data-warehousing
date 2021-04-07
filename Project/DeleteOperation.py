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

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

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

    def delete_nodes(self,k,q):
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1  
            while(level<k):
                p=p.child
                level+=1
            p.child=p.child.child
    def delete_allnodes(self,q):
        for a in q:
            a.child=None

    def saved_tree(self,q,tablename,heightoftree):
        saved2=[]
        saved2.append(len(q))
        saved2.append(heightoftree)
        saved2.append(tablename)
        while(len(q)!=0):
            z=q[0]
            if (z!=None):
                saved2.append(z.data)
                q.append(z.child)
                q.remove(z)
            else:
                break

        n = saved2[0]
        updated_list = saved2[3:]
        z = [updated_list[i:i + n] for i in range(0, len(updated_list), n)]
        x.field_names = z[0]
        data_rows = z[1:]
        for i in range(len(data_rows)):
            x.add_row(data_rows[i])
        print(x)
        x.clear_rows()
        return saved2

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.data))

        if self.children:
            for children in self.children:
                children.print_tree()
        if self.child:
            self.child.print_tree()

def delete_operation(saved,conattribute,convalue,condition):
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
    tablename=root.data
    # root.print_tree()
    if conattribute:
        selectedrecord=[]
        root.get_allnodeswithcon(heightoftree,q,conattribute,convalue,condition,selectedrecord)
        for b in selectedrecord:
            b-=selectedrecord.index(b)
            root.delete_nodes(b,q)
        heightoftree-=len(selectedrecord)
        # root.print_tree()
        final_list = root.saved_tree(q,tablename,heightoftree)
        return final_list
    else:
        root.delete_allnodes(q)
        heightoftree=1
        final_list = root.saved_tree(q,tablename,heightoftree)
        return final_list

if __name__ == '__main__':

    conattribute = 'Contact'
    condition = '='
    convalue = 54556
    saved = [4, 5,'Student', 'StudentID', 'Name', 'Grade', 'Contact', '123', 'Piyush', 'ABC', 23546, '234', 'Nirmal', 'ACB', 54556, '345', 'Falgun', 'ACA', 74656, '476', 'Test', 'dfb', 23546]
    delete_operation(saved,conattribute,convalue,condition)