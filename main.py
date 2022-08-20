source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

def get_parents(data: list) -> dict:
    tree = dict()
    for parent, child in data:
        if parent is None:
            tree[child] = dict()
    return tree

def get_childs_for(parents: dict, data: list) -> dict:
    for parent, child in data:
        if parent in parents.keys():
            parents[parent][child] = dict()
    for key in parents.keys():
        get_childs_for(parents[key], data)
    return parents

def to_tree(data_in: list) -> dict:
    return get_childs_for(get_parents(data_in), data_in)

assert to_tree(source) == expected