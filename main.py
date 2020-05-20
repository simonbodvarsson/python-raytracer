import sys

from rich.progress import track

from hittable import Sphere
from hittable_list import HittableList, HitRecord
from ray import Ray
from vec3 import Vec3


# Note in the tutorial point3 and color are used as aliases for Vec3

def write_color(pixel_color):
    print(str(int(255.999 * pixel_color.x)) + " " + \
          str(int(255.999 * pixel_color.y)) + " " + \
          str(int(255.999 * pixel_color.z)) + " ")


def ray_color(r, world):
    rec = HitRecord(None, None, None)
    if world.hit(r, 0, float('inf'), rec):
        return 0.5 * (rec.normal + Vec3(1, 1, 1))

    unit_direction = r.dir.unit_vector()
    # Since unit length: -1.0 <= y <= 1.0
    t = 0.5 * (unit_direction.y + 1)
    # Linearly interpolate between white and blue according to y-coordinate
    return (1 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.dir.length_squared()
    half_b = oc.dot(r.dir)
    c = oc.length_squared() - radius ** 2
    discriminant = half_b * half_b - a * c
    if discriminant < 0:
        return -1.0
    else:
        # If a positive t exists s.t. a*t**2 + b*t + c = 0, then
        # the ray intersects with the sphere in front of the camera.
        return (-half_b - discriminant ** 0.5) / a


def main():
    aspect_ratio = 16 / 9
    image_width = 384
    image_height = int(image_width // aspect_ratio)

    print("P3")
    print(str(image_width) + " " + str(image_height) + "\n255")

    # Set height of the viewport to 2 units
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    # Set distance from camera center (or eye) to viewport to 1 unit (in Z coordinate).
    focal_length = 1.0

    # Focal point
    origin = Vec3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)
    # print("lower_left_corner:", lower_left_corner)

    world = HittableList()
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    # Iterate through pixels of the output image
    for j in track(range(image_height - 1, -1, -1)):
        # print("Scanlines remaining: " + str(j), file=sys.stderr)
        for i in range(0, image_width):
            # Cast a ray through each pixel of the viewport
            u = i / (image_width - 1)
            v = j / (image_height - 1)

            # Why do we need to subtract the origin?
            r = Ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            # pixel_color = ray_color(r)

            pixel_color = ray_color(r, world)

            write_color(pixel_color)

            # print(str(ir) + " " + str(ig) + " " + str(ib))
    print("Done", file=sys.stderr)


if __name__ == '__main__':
    main()
