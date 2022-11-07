class FamilyTree:
    def __init__(self, lines):
        self.names = lines
        self.parents = set()
        self.family = dict()

    def make_family(self):
        for line in self.names:
            child, parent = line.split()
            if child == parent:
                raise Exception("Same name")
            if parent in self.family.keys():
                self.family[parent].append(child)
            else:
                self.family.update({parent: [child]})

    def find_parents(self):
        child = set()
        all = set()
        for person in self.family.keys():
            all.add(person)
            for children in self.family.values():
                if person in children:
                    child.add(person)
        self.parents = all - child

def print_family_tree(people, parents, depth=0):
    for person in parents:
        print("  "*depth+person)
        print_family_tree(people, people.get(person,""), depth+1)