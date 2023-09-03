class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

def create_linked_list(input_str):
    nodes = {}
    num_nodes, pairs_str = input_str.split(' ')
    num_nodes = list(range(1, int(num_nodes) + 1))
    pairs = pairs_str.split(',')
    
    for pair in pairs:
        src, dest = map(int, pair.split('-'))
        if src not in nodes:
            nodes[src] = Node(src)
        if dest not in nodes:
            nodes[dest] = Node(dest)

        nodes[src].next = nodes[dest]
        nodes[dest].prev = nodes[src]

        if src in num_nodes:
            num_nodes.remove(src)
        if dest in num_nodes:
            num_nodes.remove(dest)
            
    for num in num_nodes:
        nodes[num] = Node(num)
    
    return nodes

def organize_sets(nodes):
    visited = set()
    sets = []
    
    for node in nodes.values():
        if node.value not in visited:
            current = node
            new_set = DoublyLinkedList()
            
            while current is not None:
                if current.prev is not None and current.prev.value not in visited:
                    current = current.prev
                    continue
                
                visited.add(current.value)
                new_set_node = Node(current.value)
                if new_set.head is None:
                    new_set.head = new_set_node
                else:
                    temp = new_set.head
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = new_set_node
                
                current = current.next
            
            sets.append(new_set)
    
    return sets

def print_sets(sets):
    sorted_sets = sorted(sets, key=lambda linked_list: linked_list.head.value)
    included_nodes = set()
    count = 0

    for i, linked_list in enumerate(sorted_sets, start=1):
        new_connection = []
        current = linked_list.head

        while current is not None:
            if current.value not in included_nodes:
                new_connection.append(current.value)
                included_nodes.add(current.value)
            current = current.next

        if new_connection:
            count += 1
            print(f"{count}: ", end="")
            print("->".join(map(str, new_connection)))
            
    print(f"Number of train(s): {count}")

input_str = input("Enter input: ")
nodes = create_linked_list(input_str)
sets = organize_sets(nodes)
print_sets(sets)