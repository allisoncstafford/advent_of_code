# find the intersection point closest to the central port.
# close = Manhattan distance

def get_pts(directions):
    """From relative directions (eg. right 8, up 5, left 5, down 3),
    creates a list of grid points crossed.

    Args:
        directions: list of relative directions
    
    Returns:
        list of (x, y) coordinate tuples (integer values) on the path.
    """
    path = []
    loc = (0, 0)
    path.append(loc)

    for direction in directions:
        cardinal_dir = direction[0]
        length = int(direction[1:])
        if cardinal_dir == 'U':  
            for _ in range(length):
                loc = move_up(loc)
                path.append((loc))
        elif cardinal_dir == 'D':  
            for _ in range(length):
                loc = move_down(loc)
                path.append((loc))
        elif cardinal_dir == 'R':  
            for _ in range(length):
                loc = move_right(loc)
                path.append((loc))
        elif cardinal_dir == 'L':  
            for _ in range(length):
                loc = move_left(loc)
                path.append((loc))
    return path


def move_up(loc):
    """increments the location for upward movement.
    """ 
    return (loc[0], loc[1] + 1)


def move_down(loc):
    """increments the location for downward movement.
    """ 
    return (loc[0], loc[1] - 1)


def move_right(loc):
    """increments the location for rightward movement.
    """ 
    return (loc[0] + 1, loc[1])


def move_left(loc):
    """increments the location for leftward movement.
    """ 
    return (loc[0] - 1, loc[1])


def get_directions(filename):
    """gets the directions from the file
    
    Args:
        filename: name of the file

    Returns: 
        a list containing lists of the directions eg. return[0] is the list of
        directions from the first line of the file. return[1] is the list of
        directions from the second line of the file.
    """
    text_file = open(filename, "r")
    input_strs = text_file.readlines()
    text_file.close()
    directions = []
    for input_str in input_strs:
        directions.append(input_str.split(','))
    return directions


def get_intersections(path1, path2):
    """returns a list of the intersection points between the two paths

    Args:
        path1: one path (list of tuples with consecutive integer x, y coords)
        path2: second path (see above)
    
    Returns:
        a list of all overlapping tuples from the two paths
    """
    intersects = []
    for pt in path1:
        if pt in path2 and pt != (0,0):
            intersects.append(pt)
    return intersects


def get_closest_dist(pts):
    """returns the closest point from the list of intersections. Uses
    Manhattan Distance as metric for closeness.

    Args:
        pts: a list of (x, y) tuples

    Returns
        the manhattan distance from (0,0) of the closest pt in pts
    """
    dists = [(abs(pt[0]) + abs(pt[1])) for pt in pts]
    return min(dists)


def get_closest_intersection_pt_dist(path1, path2):
    """Returns the manhattan distance from the start location to the closest 
    intersection point.

    Args:
        path1: the first path (list of consecutive (x,y) tuples)
        path2: the secong path
    
    Returns:
        int of lowest manhattan distance for an intersection
    """
    pts1 = get_pts(path1)
    pts2 = get_pts(path2)
    intersections = get_intersections(pts1, pts2)
    return get_closest_dist(intersections)
    

def main():
    directions = get_directions('day3_input.txt')
    print(get_closest_intersection_pt_dist(directions[0], directions[1]))


if __name__ == "__main__":
    main()