class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = [] if children is None else children

    @staticmethod
    def convert_to_str(node, level=0):
        s = '-'*level  + str(node.data) + '\n'
        for kid in node.children:
            s += Node.convert_to_str(kid, level = level+1)
        return  s

    def __str__(self):
        return Node.convert_to_str(self)


if __name__ == '__main__':
    leaf4 = Node(4)
    leaf5 = Node(5)
    leaf3 = Node(3)
    node1 = Node(1, [leaf4, leaf5])
    node2 = Node(2, [node1, leaf3])
    print(node2)
