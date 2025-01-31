import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def graph3d(G, num_nodes):

    # Initialize 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Get node positions
    pos = nx.get_node_attributes(G, 'pos')

    # Draw nodes
    xs = [pos[v][0] for v in G.nodes()]
    ys = [pos[v][1] for v in G.nodes()]
    zs = [pos[v][2] for v in G.nodes()]
    ax.scatter(xs, ys, zs, c='r', s=100, alpha=0.7)

    # Draw edges
    for edge in G.edges():
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, c='gray', alpha=0.5)

    # Label plot
    ax.set_title('ITE')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    # Display graph
    plt.tight_layout()
    plt.show()



def getITEGraph():

    # Initialize graph
    G = nx.Graph()

    # Floor 1 nodes
    floorOneLoopOneNodes = [("FrontDr", {"pos": [  -1,   0,   0]}),
                            ("FrontEn", {"pos": [   0,   0,   0]}),
                            ("F1_L1_1", {"pos": [   0,-0.5,   0]}),
                            ("F1_L1_2", {"pos": [  -1,-0.5,   0]}),
                            ("F1_L1_3", {"pos": [  -1,-1.5,   0]}),
                            ("F1_L1_4", {"pos": [   0,-1.5,   0]}),
                            ("Lab 1  ", {"pos": [   0,  -2,   0]}),
                            ("F1_L1_5", {"pos": [   1,-1.5,   0]}),
                            ("Lab 2  ", {"pos": [   1,  -2,   0]}),
                            ("F1_L1_6", {"pos": [   3,-1.5,   0]}),
                            ("F1_L1_7", {"pos": [   3,-0.5,   0]})]
    G.add_nodes_from(floorOneLoopOneNodes)

    floorOneLoopTwoNodes = [("FrontDr", {"pos": [  -1,   0,   0]}),
                            ("FrontEn", {"pos": [   0,   0,   0]}),
                            ("F1_L2_1", {"pos": [   0,   2,   0]}),
                            ("F1_L2_2", {"pos": [   1,   2,   0]}),
                            ("F1_L2_3", {"pos": [   2,   2,   0]}),
                            ("ITE 119", {"pos": [   2,   3,   0]}),
                            ("F1_L2_4", {"pos": [   3,   2,   0]}),
                            ("F1_L2_5", {"pos": [   3,1.25,   0]}),
                            ("ITE 125", {"pos": [   4,1.25,   0]}),
                            ("F1_L2_6", {"pos": [   3,0.75,   0]}),
                            ("ITE 127", {"pos": [   4,0.75,   0]}),
                            ("BackExt", {"pos": [   3,   0,   0]}),
                            ("BackDor", {"pos": [   4,   0,   0]})]
    G.add_nodes_from(floorOneLoopTwoNodes)


    # Floor 1 edges
    floorTwoLoopOneEdges = [("FrontDr", "FrontEn"),
                            ("FrontEn", "F1_L1_1"), 
                            ("F1_L1_1", "F1_L1_2"), 
                            ("F1_L1_2", "F1_L1_3"), 
                            ("F1_L1_3", "F1_L1_4"), 
                            ("F1_L1_4", "Lab 1  "),
                            ("F1_L1_4", "F1_L1_5"), 
                            ("F1_L1_5", "Lab 2  "),
                            ("F1_L1_5", "F1_L1_6"),
                            ("F1_L1_6", "F1_L1_7"),
                            ("F1_L1_7", "F1_L1_1"),
                            ("F1_L1_7", "BackExt"),
                            ("BackExt", "BackDor")]
    G.add_edges_from(floorTwoLoopOneEdges)

    floorTwoLoopTwoEdges = [("FrontDr", "FrontEn"),
                            ("FrontEn", "F1_L2_1"),
                            ("F1_L2_1", "F1_L2_2"),
                            ("F1_L2_2", "F1_L2_3"),
                            ("F1_L2_3", "F1_L2_4"),
                            ("F1_L2_3", "ITE 119"),
                            ("F1_L2_4", "F1_L2_5"),
                            ("F1_L2_5", "F1_L2_6"),
                            ("F1_L2_5", "ITE 125"),
                            ("F1_L2_5", "F1_L2_6"),
                            ("F1_L2_6", "ITE 127"),
                            ("F1_L2_6", "BackExt"),
                            ("BackExt", "BackDor")]
    G.add_edges_from(floorTwoLoopTwoEdges)

    # Floor C Nodes
    floorCNodes = [("FrontEn", {"pos": [   0,   0,   0]}),
                   ("CLandin", {"pos": [   3,   0,  -1]}),
                   ("FC_1",    {"pos": [ 3.5,   0,  -1]}),
                   ("FC_2",    {"pos": [ 3.5,-0.5,  -1]})]

    G.add_nodes_from(floorCNodes)

    # Floor C Edges
    floorCEdges = [("FrontEn", "CLandin"),
                   ("CLandin", "FC_1"),
                   ("FC_1"   , "FC_2")]
    G.add_edges_from(floorCEdges)

    return G

if __name__ == '__main__':
    graph = getITEGraph()
    graph3d(graph, 2)
