from abc import ABC

from ray import Ray
from vec3 import Vec3


class Material(ABC):
    pass


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, hit_record):
        scatter_direction = hit_record.normal + Vec3.random_unit_vector()
        scattered = Ray(hit_record.p, scatter_direction)
        attenuation = self.albedo
        return True, scattered, attenuation


class Metal(Material):
    def __init__(self, albedo, fuzz=0):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, r_in, hit_record):
        reflected = r_in.dir.unit_vector().reflect(hit_record.normal)
        scattered = Ray(hit_record.p, reflected + self.fuzz*Vec3.random_in_unit_sphere())
        attenuation = self.albedo
        return scattered.dir.dot(hit_record.normal) > 0, scattered, attenuation
