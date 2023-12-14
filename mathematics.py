def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

def calculate_circumference_of_circle(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

def calculate_volume_of_sphere(radius):
    pi = 3.14159
    volume = (4 / 3) * pi * radius * radius * radius
    return volume

# Example usage
if __name__ == "__main__":
    radius = 5
    area = calculate_area_of_circle(radius)
    circumference = calculate_circumference_of_circle(radius)
    volume = calculate_volume_of_sphere(radius)

    print(f"Radius: {radius}")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    print(f"Volume: {volume}")
