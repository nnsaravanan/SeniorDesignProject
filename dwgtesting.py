import ezdxf
import matplotlib.pyplot as plt

def plot_dwg(file_path):
    # Load the DWG file
    dwg = ezdxf.readfile(file_path)
    
    # Set up the plot
    plt.figure()
    ax = plt.gca()
    
    # Loop through each layout in the DWG (usually 'Model' space contains the drawing)
    for layout in dwg.layouts:
        for entity in layout:
            if entity.dxftype() == 'LINE':
                # Extract the line start and end points
                x1, y1, z1 = entity.dxf.start
                x2, y2, z2 = entity.dxf.end
                plt.plot([x1, x2], [y1, y2], color="black")
            elif entity.dxftype() == 'CIRCLE':
                # Extract the circle center and radius
                center = entity.dxf.center
                radius = entity.dxf.radius
                circle = plt.Circle((center[0], center[1]), radius, color="blue", fill=False)
                ax.add_patch(circle)
            elif entity.dxftype() == 'ARC':
                # Extract arc center, radius, and angles
                center = entity.dxf.center
                radius = entity.dxf.radius
                start_angle = entity.dxf.start_angle
                end_angle = entity.dxf.end_angle
                arc = plt.Arc((center[0], center[1]), radius*2, radius*2, angle=0,
                              theta1=start_angle, theta2=end_angle, color="red")
                ax.add_patch(arc)
            # Add more entity types as needed (e.g., POLYLINE, LWPOLYLINE)

    # Set aspect ratio and show the plot
    ax.set_aspect('equal')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DWG File Display")
    plt.show()

# Replace 'path_to_your_file.dwg' with your DWG file path
plot_dwg('floorplan2.dxf')
