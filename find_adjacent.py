import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please specify xyz input file and adjacency outfile.")
    else:
        inname = sys.argv[1]
        outname = sys.argv[2]


# parses the coordinates from an xyz file
def parse_xyz(xyz_name):
    # make a new datatype (numpy.void)
    xyz_row_format = np.dtype(dtype=[('element', 'U1'), ('x', 'f8'), ('y', 'f8'),('z', 'f8')])
    xyz = np.genfromtxt(xyz_name, skip_header=2, dtype=xyz_row_format)
    return xyz

# throws out all atoms that are not carbon, and returns a numpy array
def keep_carbons(xyz):
    n_cs = 0
    for row in xyz:
        if row[0] == 'C':
            n_cs += 1

    current = 0
    c_xyz = np.empty((n_cs, 3))
    for row in xyz:
        if row[0] == 'C':
            coords = np.array([row[1], row[2], row[3]])
            c_xyz[current] = coords
            current += 1
    
    return c_xyz

# finds distance between two vectors
def find_dist(xyz1, xyz2):
    difference = xyz1 - xyz2
    distance = np.linalg.norm(difference)
    return distance

# builds adjacency matrix, with no cutoffs
def find_adjacency(xyz):
    n_cs = len(xyz)
    adjacency = np.zeros((n_cs, n_cs))
    for i, row1 in enumerate(xyz):
        for j, row2 in enumerate(xyz):
            if i == j:
                continue
            dist = find_dist(row1, row2)
            adjacency[i,j] = dist
    #print(adjacency)
    return adjacency

# build a stripped down connectivity matrix, based on some cutoff
def strip_down(adjacency, cutoff = 2.0):
    adjacency = np.where(adjacency <= cutoff, adjacency, 0)
    adjacency = np.where(adjacency < 0.1, adjacency, 1)
    return adjacency

# plots the adjacency matrix, with some cutoff
def plot_graph(adjacency, cutoff = 2.0):
    graph = nx.from_numpy_matrix(adjacency, create_using=nx.MultiGraph)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")
    #plt.show()

# outputs the bonds csv
def output_csv(mat, outname):
    np.savetxt(outname, mat, delimiter=",", fmt='%u')


if __name__ == "__main__":
    xyz = parse_xyz(inname)
    c_xyz = keep_carbons(xyz)
    adjacency = find_adjacency(c_xyz)
    print(adjacency)
    adjacency = strip_down(adjacency)
    plot_graph(adjacency) 
    output_csv(adjacency, outname)

