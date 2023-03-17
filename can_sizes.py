import math


def main():

    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#6Z"
    radius = 5.4
    height = 8.89
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")

    name = "#303"
    radius = 8.1
    height = 11.11
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print(f"{name} {storage:.2f}")


def compute_volume(radius, height):
    """Compute and return the volume of a cylinder."""
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder."""
    surface = 2 * math.pi * radius * (radius + height)
    return surface


def storage_efficiency(volume, surface):
    """Compute and return the storage efficiency."""
    storage = volume/surface
    return storage


"""Start this program"""
if __name__ == "__main__":
    main()