graph = {
    "you": [ 'bob', 'alice', 'claire' ],
    'alice': [ 'peggy' ],
    'bob': ['peggy', 'anuj' ],
    'claire': ['tom', 'jhonny'],
    'anuj': [ 'kenny' ]
}

mango_sellers = [ 'kenny', 'tom' ]
def is_mango_seller( node ):
    return node in mango_sellers

def find_closest( graph, start_node, satisfies_condition ):
    nodes_to_check = [ start_node ]
    checked_nodes = []

    path_parents_pointers = {} # saving path to calculate if we find element
    closest = None
    while len( nodes_to_check ):
        node_to_check = nodes_to_check.pop(0)
        if not node_to_check in checked_nodes: 
            if satisfies_condition( node_to_check ):
                closest = node_to_check
                break
            else:
                children_nodes = graph[ node_to_check ] if node_to_check in graph else []
                for child_node in children_nodes:
                    nodes_to_check.append( child_node )
                    path_parents_pointers[ child_node ] = node_to_check
                checked_nodes.append( node_to_check )

    path = calculate_path( start_node, closest, path_parents_pointers ) 
    return (closest, path)

def calculate_path( start_node, finish_node, path_parents_pointers ):
    path = [ finish_node ]
    curr_node = finish_node
    while curr_node != start_node:
        curr_node = path_parents_pointers[ curr_node ]
        path.insert( 0, curr_node )
    return path


print( find_closest( graph, 'you', is_mango_seller ) )