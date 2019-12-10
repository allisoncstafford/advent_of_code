from matplotlib import pyplot as plt
from day3_pt1 import get_pts, get_directions


def main():
    directions = get_directions('day3_input.txt')
    create_accidental_icicle_graph(directions[0], directions[1])
    create_accidental_mountains_graph(directions[0], directions[1])
    create_wire_graph(directions[0], directions[1])


def create_accidental_icicle_graph(dir1, dir2):
    fig, ax = plt.subplots(figsize=(20,20))
    ax.plot(dir1, color='blue', linewidth=5)
    ax.plot(dir2, color='cyan', linewidth=5)
    fig.savefig('day3_icicles.png')


def create_accidental_mountains_graph(dir1, dir2):
    fig, ax = plt.subplots(figsize=(20,20))
    pts1 = get_pts(dir1)
    pts2 = get_pts(dir2)
    ax.plot(pts1, color='#013220', linewidth=5)
    ax.plot(pts2, color='green', linewidth=5)
    fig.savefig('day3_mountains.png')


def create_wire_graph(dir1, dir2):
    # convert directions to points
    pts1 = get_pts(dir1)
    pts2 = get_pts(dir2)

    # separate x and y for each set
    x1 = [x[0] for x in pts1]
    y1 = [x[1] for x in pts1]
    x2 = [x[0] for x in pts2]
    y2 = [x[1] for x in pts2]

    # graph
    fig, ax = plt.subplots(figsize=(20,20))
    ax.plot(x1, y1, color='red', linewidth=5)
    ax.plot(x2, y2, color='green', linewidth=5)
    fig.savefig('day3_image.png')



if __name__ == "__main__":
    main()

