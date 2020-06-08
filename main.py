import sys
from math import sqrt
from random import random

from camera import Camera
from hittable import Sphere
from hittable_list import HittableList, HitRecord
from material import Lambertian, Metal, Dielectric
from vec3 import Vec3


# Note in the tutorial point3 and color are used as aliases for Vec3

def write_color(pixel_color, samples_per_pixel):
    # Divide the color by the number of samples passed through this pixel
    scale = 1.0 / samples_per_pixel

    r = scale * pixel_color.x
    g = scale * pixel_color.y
    b = scale * pixel_color.z

    # gamma-correct  for gamma = 2.0
    r = sqrt(r)
    g = sqrt(g)
    b = sqrt(b)

    # Clamp to [0, 0.999]
    r = max(0, min(r, 0.999))
    g = max(0, min(g, 0.999))
    b = max(0, min(b, 0.999))

    print(str(int(256 * r)) + " " +
          str(int(256 * g)) + " " +
          str(int(256 * b)) + " ")


def ray_color(r, world, depth):
    # Check if max depth of recursion is exceeded.
    if depth <= 0:
        return Vec3(0, 0, 0)

    rec = HitRecord(None, None, None, None)
    if world.hit(r, 0.001, float('inf'), rec):
        did_scatter, scattered, attenuation = rec.material.scatter(r, rec)
        if did_scatter:
            # print("attenuation", attenuation)
            # print('scattered', scattered)
            return attenuation * ray_color(scattered, world, depth - 1)
        return Vec3(0, 0, 0)
        # # target = rec.p + rec.normal + Vec3.random_unit_vector()
        # target = rec.p + rec.normal + Vec3.random_in_hemisphere(rec.normal)
        # return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth - 1)

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
    image_width = 800  # 384
    image_height = int(image_width // aspect_ratio)
    samples_per_pixel = 100  # 20
    max_depth = 100  # 20

    world = HittableList()
    # world.add(Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.7, 0.3, 0.3))))
    world.add(Sphere(Vec3(0, 0, -1.5), 0.5, Lambertian(Vec3(0.2, 0.8, 0.3))))
    world.add(Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0))))

    # world.add(Sphere(Vec3(1, 0, -1), 0.5, Metal(Vec3(.8, .6, .2))))
    # world.add(Sphere(Vec3(-1, 0, -1), 0.5, Metal(Vec3(.8, .8, .8))))

    world.add(Sphere(Vec3(1, 0, -1.5), 0.5, Metal(Vec3(.8, .6, .2))))
    world.add(Sphere(Vec3(-1, 0, -1.5), 0.5, Metal(Vec3(.8, .8, .8), fuzz=0.3)))

    # Hollow glass sphere
    world.add(Sphere(Vec3(2, 0, -1.5), 0.5, Dielectric(1.5)))
    world.add(Sphere(Vec3(2, 0, -1.5), -0.45, Dielectric(1.5)))

    # Glass sphere
    world.add(Sphere(Vec3(-2, 0, -1.5), 0.5, Dielectric(1.5)))

    cam = Camera()

    print("P3")
    print(str(image_width) + " " + str(image_height) + "\n255")

    # Iterate through pixels of the output image
    # Cast a ray through each pixel of the viewport
    for j in range(image_height - 1, -1, -1):
        print("Scanlines remaining: " + str(j), end="\r", file=sys.stderr)
        for i in range(0, image_width):

            pixel_color = Vec3(0, 0, 0)
            for s in range(samples_per_pixel):
                u = (i + random()) / (image_width - 1)
                v = (j + random()) / (image_height - 1)

                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)

            write_color(pixel_color, samples_per_pixel)
    print("\nDone", file=sys.stderr)


if __name__ == '__main__':
    main()
