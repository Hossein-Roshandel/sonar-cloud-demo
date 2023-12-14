def calculate_area(r):
    # Code smell: Poor variable name
    a = 3.14159 * r * r
    return a

def calculate_volume(radius):
    # Code smell: Magic number without explanation
    volume = 4/3 * 3.14159 * radius ** 3
    return volume

def print_result(radius):
    area = calculate_area(radius)
    volume = calculate_volume(radius)
    
    # Code smell: Inconsistent formatting
    print(f"Radius: {radius}")
    print("Area: ", area)
    print("Volume: ", volume)

# Code smell: Unused variable
value = 10

if __name__ == "__main__":
    # Code smell: Hard-coded value
    radius = 5
    print_result(radius)
    
    print_result(5)
