import math

def count_illuminated_nodes_corrected(x1, y1, x2, y2, xl, yl, r):
    count = 0  # Counter for illuminated nodes
    
    # Loop through each potential y-coordinate that could intersect the circle
    for y in range(max(y1, yl - r), min(y2, yl + r) + 1):
        # Calculate the corresponding x-range for each y-coordinate within the circle
        dy = y - yl
        dx = math.sqrt(r ** 2 - dy ** 2)
        
        # Calculate the leftmost and rightmost x-coordinates that are within the circle for this y-coordinate
        x_left = max(x1, int(math.ceil(xl - dx)))
        x_right = min(x2, int(math.floor(xl + dx)))
        
        # Add the number of points between x_left and x_right to the count
        if x_left <= x_right:
            count += (x_right - x_left + 1)
    
    return count


# Example usage:
x1, y1 = 0, 0  # Bottom left corner of the grid
x2, y2 = 1, 2  # Top right corner of the grid
xl, yl = 0, 0  # Coordinates of the beacon
r = 1  # Radius of illumination

print(count_illuminated_nodes_corrected(x1, y1, x2, y2, xl, yl, r))
