from abc import ABC
from math import sqrt
from random import random

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
        scattered = Ray(hit_record.p, reflected + self.fuzz * Vec3.random_in_unit_sphere())
        attenuation = self.albedo
        return scattered.dir.dot(hit_record.normal) > 0, scattered, attenuation


def schlick(cosine, idx):
    r0 = (1 - idx) / (1 + idx)
    r0 = r0 ** 2
    return r0 + (1 - r0) * pow((1 - cosine), 5)


class Dielectric(Material):
    def __init__(self, refraction_index):
        # air: r=1.0
        # glass: r=1.3-1.7
        # diamond: r=2.4
        self.refraction_index = refraction_index

    def scatter(self, r_in, hit_record):
        attenuation = Vec3(1.0, 1.0, 1.0)
        if hit_record.is_inside:
            refraction_ratio = self.refraction_index
        else:
            refraction_ratio = 1.0 / self.refraction_index
        unit_direction = r_in.dir.unit_vector()

        cos_theta = min(1.0, (-unit_direction.dot(hit_record.normal)))
        sin_theta = sqrt(1.0 - cos_theta * cos_theta)

        # Reflectivity increases with angle.
        reflect_prob = schlick(cos_theta, refraction_ratio)

        # If refraction_ratio * sin_theta > 1.0, the ray must be reflected, otherwise it is reflected with
        # probability reflect_prob
        if refraction_ratio * sin_theta > 1.0 or random() < reflect_prob:
            # Ray cannot refract and must be reflected
            reflected = unit_direction.reflect(hit_record.normal)
            scattered = Ray(hit_record.p, reflected)
            return True, scattered, attenuation

        refracted = unit_direction.refract(hit_record.normal, refraction_ratio)
        scattered = Ray(hit_record.p, refracted)
        return True, scattered, attenuation
