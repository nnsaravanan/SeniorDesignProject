import ezdxf
import networkx as nx

# Load the DXF file
doc = ezdxf.readfile("path/to/floorplan.dxf")
modelspace = doc.modelspace()

# Extract rooms and hallways
rooms = []  # This will hold room entities (likely polygons)
hallways = []  # This will hold hallway entities (lines or polygons)

for entity in modelspace:
    if entity.dxftype() == 'LWPOLYLINE':
        if "ROOM" in entity.dxf.layer:
            rooms.append(entity)
        elif "HALLWAY" in entity.dxf.layer:
            hallways.append(entity)

# Create a graph to represent connections between rooms
G = nx.Graph()

# Add rooms as nodes, using the center of each room polygon as a node position
for idx, room in enumerate(rooms):
    vertices = room.get_points("xy")
    x_coords, y_coords = zip(*vertices)
    room_center = (sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords))
    G.add_node(idx, pos=room_center)

# Add hallways as edges between room nodes based on spatial proximity
for hallway in hallways:
    hallway_center = hallway.get_center()  # Approximate center of hallway
    # Connect rooms that are near this hallway
    for room_idx, room in enumerate(rooms):
        room_center = G.nodes[room_idx]["pos"]
        if is_near(hallway_center, room_center):  # Define `is_near` based on distance
            G.add_edge(room_idx, room_idx + 1)  # This should connect appropriate rooms

# Define starting and target room indices (based on room numbering)
start_room = 0  # Example start room
target_room = len(rooms) - 1  # Example target room

# Find the shortest path
try:
    path = nx.shortest_path(G, source=start_room, target=target_room)
    print("Path from room {} to room {}: {}".format(start_room, target_room, path))
except nx.NetworkXNoPath:
    print("No path found between rooms.")
