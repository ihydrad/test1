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

def get_parants(data: list) -> dict:
    tree = dict()
    for parant, child in data:
        if parant is None:
            tree[child] = dict()
    return tree

def get_childs_for(parents: dict, data: list) -> dict:
    for parant, child in data:
        if parant in parents.keys():
            parents[parant][child] = dict()
    for key in parents.keys():
        get_childs_for(parents[key], data)
    return parents

def to_tree(data_in: list) -> dict:
    return get_childs_for(get_parants(data_in), data_in)

assert to_tree(source) == expected