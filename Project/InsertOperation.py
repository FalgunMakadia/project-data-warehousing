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

    def insert_node(self,heightoftree,q,attributes,newvalues):
        length = len(q)
        for i in range(length):
            p=q[i]
            level=1
            while(level<heightoftree):
                p=p.child
                level+=1
            p.add_child(TreeNode(newvalues[i]))

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.data))

        if self.children:
            for children in self.children:
                children.print_tree()
        if self.child:
            self.child.print_tree()

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

def insert_operation(saved,attributes,newvalues):
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
    root.insert_node(heightoftree,q,attributes,newvalues)
    heightoftree+=1
    tablename = root.data
    final_list = root.saved_tree(q,tablename,heightoftree)
    return final_list

if __name__ == '__main__':

    attributes =['StudentID', 'Name', 'Grade', 'Contact']
    condition='='
    conattributes='Contact'
    convalues=23546
    newvalues=['T123', 'TPiyush', 'TABC', 123546]
    saved = [4, 5,'Student', 'StudentID', 'Name', 'Grade', 'Contact', '123', 'Piyush', 'ABC', 23546, '234', 'Nirmal', 'ACB', 54556, '345', 'Falgun', 'ACA', 74656, '476', 'Test', 'dfb', 23546]
    insert_operation(saved,attributes,newvalues)