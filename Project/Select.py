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
            if e.data == convalue:
                j.append(level)
                print(len(j))
                e=e.child
                level+=1
            else:
                e=e.child
                level+=1
        for b in j:
            root.get_allnodes(b,q)

def get_nodes(self,k,attributes):
       q=[]
       for a in root.children:
           if a.data in attributes:
               q.append(a)
       root.get_allnodes(k,q)
         
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


def select(self,attributes,condition,conattributes,convalues):
    if not attributes:
        if not conattributes:
            q=root.children
            root.get_allnodes(heightoftree,q)
        else:
            q=root.children
            root.get_allnodeswithcon(heightoftree,q,conatribute,convalue)           
    else:
        if not conattributes:
            root.get_nodes(self,heigtoftree,attributes)
        else:
            root.get_nodeswithcon(heightoftree,q,conatribute,convalue,attributes)
