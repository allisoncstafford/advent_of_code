from day3_pt1 import get_pts, get_intersections, get_directions


def get_shortest_step_ct(dir1, dir2):
    """returns the shortest step count to intersection point between the paths
    described by the argument directions

    Args:
        dir1: list of directions for first path
        dir2: list of directions for second path

    Returns:
        the minimum number of steps required to get to an intersection point
        of the two paths
    """
    pts1 = get_pts(dir1)
    pts2 = get_pts(dir2)
    intersections = get_intersections(pts1, pts2)
    return get_fewest_steps(pts1, pts2, intersections)

def get_fewest_steps(pts1, pts2, intersections):
    """Returns the minimum number of steps required to get to an intersection
    point between the two paths.

    Args:
        pts1: the list of points along the first path
        pts2: the list of points along the second path
        intersections: the list of points where the paths intersect
    """
    # make a dictionary of the number of steps required to get to each
    # intersection point
    x_pt_dict = { x_pt: {'path1':0, 'path2':0, 'tot':0} for x_pt in intersections}
    intersection_steps = []

    for intersection in intersections:
        x_pt_dict[intersection]['path1'] = pts1.index(intersection)
        x_pt_dict[intersection]['path2'] = pts2.index(intersection)
        x_pt_dict[intersection]['tot'] = (x_pt_dict[intersection]['path1'] 
                                        + x_pt_dict[intersection]['path2'])
        intersection_steps.append(x_pt_dict[intersection]['tot'])
    return min(intersection_steps)

def main():
    directions = get_directions('day3_input.txt')
    print(get_shortest_step_ct(directions[0], directions[1]))


if __name__ == "__main__":
    main()