#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx



def parse(xyz_name):
    # make a new datatype (numpy.void)
    xyz_row_format = np.dtype(dtype=[('element', 'U1'), ('x', 'f8'), ('y', 'f8'),('z', 'f8')])
    xyz = np.genfromtxt(xyz_name, skip_header=2, dtype=xyz_row_format)
    return xyz

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

def find_dist(xyz1, xyz2):
    difference = xyz1 - xyz2
    distance = np.linalg.norm(difference)
    return distance

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


def find_bonds(adjacency, cutoff = 2.0):
    n_cs = len(adjacency)
    bonds = []
    for i in range(n_cs):
        neighbs = []
        for j in range(n_cs):
            if i == j:
                continue
            if adjacency[i,j] < cutoff:
                neighbs.append(j)
        bonds.append(neighbs)
    #print(bonds)
    return bonds


def plot(adjacency, cutoff = 2.0):
    adjacency = np.where(adjacency <= 2.0, adjacency, 0)
    graph = nx.from_numpy_matrix(adjacency, create_using=nx.MultiGraph)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")
    #plt.show()

def output_csv(mat, outname):
    #np.savetxt(outname, mat, delimiter=",")
    np.savetxt(outname, mat, delimiter=",", fmt='%u')


#xyz = parse('xyz/butadienyl.xyz')
#xyz = parse('xyz/benzene.xyz')
xyz = parse('xyz/c60.xyz')
c_xyz = keep_carbons(xyz)
adjacency = find_adjacency(c_xyz)
print(adjacency)
bonds = find_bonds(adjacency)
print(bonds)
plot(adjacency) 
#output_csv(bonds, "benzene_bonds.csv")
output_csv(bonds, "c60_bonds.csv")

