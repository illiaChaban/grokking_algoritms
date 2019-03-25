def find_max_value( max_space, prices, weights): #prices == values, weights == time
    step = find_min_step( weights )
    #building grid
    grid_width = int( max_space/step )
    grid_height = len(prices)
    grid = build_grid( grid_height, grid_width )

    items = prices.keys()
    for i in range(0, grid_height):
        item = items[i]
        item_price = prices[ item ]
        item_weight = weights[ item ]
        for j in range( 0, grid_width ):
            cell = grid[i][j]
            # getting previous max
            prev_max_cell = grid[i-1][j] if i > 0 else get_empty_cell()
            # getting current possible value
            curr_step_weight = step * ( j + 1 )
            weight_diff = curr_step_weight - item_weight
            remaining_weight_cell = find_remaining_weight_cell( grid, i, weight_diff, step )
            curr_val = item_price + remaining_weight_cell['price']

            if curr_val > prev_max_cell['price'] and item_weight <= curr_step_weight:
                cell['price'] = curr_val
                cell['items'] = set([item]) | remaining_weight_cell['items']
            else:
                cell['price'] = prev_max_cell['price']
                cell['items'] = prev_max_cell['items'].copy()

    solution = grid[-1][-1]

    print( solution )
    return solution

def find_remaining_weight_cell( grid, curr_i, weight_diff, step ):
    if curr_i == 0 or weight_diff <= 0:
        return get_empty_cell() 
    i = curr_i - 1
    j = int( (weight_diff / step) - 1 )
    return grid[i][j]

def get_empty_cell():
    return { 'price': 0, 'items': set() }

def find_min_step( weights ):
    return reduce( lambda x,y: x if x < y else y, weights.values() )

def build_grid( height, width ):
    grid = []
    for h in range(0,height):
        row = []
        for w in range(0,width):
            row.append( get_empty_cell() )
        grid.append(row)
    return grid

########################################
# TESTING KNAPSACK PROBLEM
########################################
prices = {
    'stereo': 3000,
    'laptop': 2000,
    'guitar': 1500,
}
weights = {
    'stereo': 4,
    'laptop': 3,
    'guitar': 1,
}
find_max_value( 4, prices, weights ) #3500

prices['iphone'] = 2000
weights['iphone'] = 1
find_max_value( 4, prices, weights ) #4000

prices['mp3_player'] = 1000
weights['mp3_player'] = 1
find_max_value( 4, prices, weights ) #4500

prices['big_diamond'] = 1000000
weights['big_diamond'] = 3.5
find_max_value( 4, prices, weights ) #1000000


values = {
    'water': 10,
    'book': 3,
    'food': 9,
    'jacket': 5,
    'camera': 6
}
weights2 = {
    'water': 3,
    'book': 1,
    'food': 2,
    'jacket': 2,
    'camera': 1
}
find_max_value( 6, values, weights2 ) #25

########################################
# TESTING TRAVEL PROBLEM
########################################
time = {
    'westminster abbey': 0.5,
    'globe theater': 0.5,
    'national gallery': 1,
    'british museum': 2,
    'st paul\'s cathedral': 0.5,
}

rating = {
    'westminster abbey': 7,
    'globe theater': 6,
    'national gallery': 9,
    'british museum': 9,
    'st paul\'s cathedral': 8,
}

find_max_value( 2, rating, time ) #24