def plot_route(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
        
        if len(lines) < 2:
            print("Error: Invalid file format")
            return
        
        try:
            x = int(lines[0])
            y = int(lines[1])
        except ValueError:
            print("Error: Invalid coordinates in file")
            return
        
        # Check if starting position is within grid
        if not (1 <= x <= 12 and 1 <= y <= 12):
            print("Error: The route is outside of the grid")
            return
        
        directions = lines[2:]
        coordinates = [(x, y)]
        
        for direction in directions:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            else:
                print(f"Error: Invalid direction '{direction}' in file")
                return
            
            coordinates.append((x, y))
            
            # Check if current position is within grid
            if not (1 <= x <= 12 and 1 <= y <= 12):
                print("Error: The route is outside of the grid")
                return
        
        # Create and display the grid
        grid = [['.' for _ in range(12)] for _ in range(12)]
        
        for i, (x_coord, y_coord) in enumerate(coordinates):
            # Convert to 0-based index for grid
            grid_x = x_coord - 1
            grid_y = y_coord - 1
            
            # Mark the position on the grid
            if i == 0:
                grid[grid_y][grid_x] = 'S'  # Start
            elif i == len(coordinates) - 1:
                grid[grid_y][grid_x] = 'E'  # End
            else:
                grid[grid_y][grid_x] = '*'  # Route
        
        # Print the grid (with y-axis inverted for display)
        print("Route plot:")
        for row in reversed(grid):
            print(' '.join(row))
        
        # Print the coordinates
        print("\nRoute coordinates:")
        for coord in coordinates:
            print(coord)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

def main():
    print("Drone Route Plotter Program")
    print("Enter route instruction files to plot routes.")
    print("Enter 'STOP' to finish.\n")
    
    while True:
        filename = input("Enter the next route instructions file or enter STOP to finish: ").strip()
        
        if filename.upper() == "STOP":
            print("Program finished.")
            break
        
        if not filename:
            continue
            
        plot_route(filename)
        print()  # Add blank line between routes

if __name__ == "__main__":
    main()
