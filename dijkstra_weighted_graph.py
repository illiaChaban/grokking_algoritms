infinity = float('inf')

graph1 = {
    "book": { "lp": 5, "poster": 0 },
    "lp":{ "guitar": 15, "drums": 20 },
    "poster": { "guitar": 30, "drums": 35 },
    "guitar": { "piano": 20 },
    "drums": { "piano": 10 },
    "piano": {}
}

graph2 = {
    "start": { 'a': 6, 'b': 2 },
    'b': { 'a': 3, 'finish': 5 },
    'a': { 'finish': 1 },
    'finish': {}
}

graph3 = {
    "start": { 'a':5, 'b':2 },
    'a': { 'c': 4, 'd': 2 },
    'b': { 'a': 8, 'd': 7 },
    'c': { 'finish': 3, 'd': 6 },
    'd': { 'finish': 1 },
    'finish': {}
}

graph4 = {
    'start': { 'a': 10 },
    'a': { 'b': 20 },
    'b': { 'c': 1, 'finish': 30 },
    'c': { 'a': 1 },
    'finish': {}
}

# graph5 = {
#     'start': { 'a': 2, 'b': 2 },
#     'a': { 'finish': 2, 'c': 2 },
#     'b': { 'a': 2 },
#     'c': { 'b': -1, 'finish': 2 },
#     'finish': {}
# }




def find_dijkstra( graph, start_node='start', finish_node='finish' ):
    # setup
    cost = {}
    parents = {}
    checked_nodes = []

    cheapest_node = start_node
    while cheapest_node:
        check_node( cheapest_node, graph, cost, parents ) #updating cost and parents
        checked_nodes.append( cheapest_node )
        cheapest_node = find_cheapest_node( cost, checked_nodes )


    final_path = calculate_path( start_node, finish_node, parents )
    print( 
        cost[finish_node],
        final_path 
    )

def calculate_path( start_node, finish_node, parents ):
    curr_node = finish_node
    path = [ finish_node ]
    while curr_node != start_node:
        parent = parents[ curr_node ]
        curr_node = parent
        path.append( parent)
    return path

def check_node( node, graph, cost, parents ):
    # print( "checking", node )
    node_cost = cost[ node ] if node in cost else 0 #starting condition
    node_children_dict = graph[ node ]
    node_children = sorted( node_children_dict, key=lambda x: node_children_dict[x] )
    # print( node_children_dict )
    for node_child in node_children:
        node_child_cost = node_children_dict[ node_child ] + node_cost
        # print( "node child cost", node_child_cost, "for", node_child, " with edge cost ", node_children_dict[ node_child ], " and prev cost ", cost[node])
        if not ( node_child in cost ):
            cost[ node_child ] = infinity
        if cost[ node_child ] > node_child_cost:
            cost[ node_child ] = node_child_cost
            parents[ node_child ] = node
            # print( "updated cost", node_child_cost, node_child )


def find_cheapest_node( cost, checked_nodes ):
    cheapest_node_cost = infinity
    cheapest_node = None
    nodes = cost.keys()
    for node in nodes:
        if node in checked_nodes: 
            continue
        if cost[node] < cheapest_node_cost:
            cheapest_node_cost = cost[node]
            cheapest_node = node
    return cheapest_node

find_dijkstra( graph1, "book", "piano" ) #35
find_dijkstra( graph2, "start", "finish" ) #6
find_dijkstra( graph3 ) #8
find_dijkstra( graph4 ) #60
# find_dijkstra( graph5 ) #4