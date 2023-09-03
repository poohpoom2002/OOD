class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Snode:
    def __init__(self, data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = None
        self.secondary_nodes = {}
        self.displayed_primary_nodes = set()

    def next_node(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def next_secondary_node(self, n, data):
        new_snode = Snode(data)
        if n in self.secondary_nodes:
            current = self.secondary_nodes[n]
            while current.next:
                current = current.next
            current.next = new_snode
        else:
            self.secondary_nodes[n] = new_snode

    def show_all(self):
        current = self.head
        while current:
            if current.data not in self.displayed_primary_nodes:
                print(current.data, ":", end=" ")
                if current.data in self.secondary_nodes:
                    secondary_current = self.secondary_nodes[current.data]
                    while secondary_current:
                        print(secondary_current.data, end=",")
                        secondary_current = secondary_current.next
                print()
                self.displayed_primary_nodes.add(current.data)
            current = current.next

inp = input("input : ").split(",")
l = link()

for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(u[1])
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0], h[1])

l.show_all()