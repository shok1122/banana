class Node:

    def __init__(self, label=''):
        self.label = label
        self.parent = None
        self.tier = 0
        self.children = []

    def set_parent(self, parent_node):
        self.parent = parent_node

    def add_child(self, label=''):
        child = Node(label)
        child.parent = self
        child.tier = child.parent.tier + 1
        self.children.append(child)
        return child

    def dump_text(self):
        tab = ''
        for i in range(self.tier):
            tab += '\t'
        print(f'{tab}{self.label}')
        for c in self.children:
            c.dump_text()

class Tree:

    def __init__(self):
        self.root = Node()

    def set_root(self, label):
        self.root.label = label
        self.parent = None

    def load(self, data):
        self.root.label = data['label']
        for c in data['children']:
            self.load_children(self.root, c)

    def load_children(self, node, child_data):
        node = node.add_child(child_data['label'])
        for c in child_data['children']:
            self.load_children(node, c)

    def dump_text(self):
        self.root.dump_text()

if __name__ == '__main__':
    tree = Tree()
    data = {
        'label':'1000',
        'children':[
            { 'label': '1100', 'children': [
                    { 'label': '1110', 'children': [] },
                    { 'label': '1120', 'children': [
                            { 'label': '1121', 'children': [] },
                            { 'label': '1122', 'children': [] },
                            { 'label': '1123', 'children': [] },
                        ]
                    },
                    { 'label': '1130', 'children': [] },
                ]
            },
            { 'label': '1200', 'children': [
                    { 'label': '1210', 'children': [
                            { 'label': '1211', 'children': [] },
                            { 'label': '1212', 'children': [] },
                        ]
                    },
                    { 'label': '1220', 'children': [] },
                    { 'label': '1230', 'children': [
                            { 'label': '1231', 'children': [] },
                            { 'label': '1232', 'children': [] },
                            { 'label': '1233', 'children': [] },
                        ]
                    },
                    { 'label': '1240', 'children': [] },
                    { 'label': '1250', 'children': [] },
                ]
            },
            { 'label': '1300', 'children': [] },
        ]
    }

    tree.load(data)

    tree.dump_text()

