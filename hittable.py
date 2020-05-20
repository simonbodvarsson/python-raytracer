from abc import ABC


class HitRecord:
    def __init__(self, p, normal, t):
        self.p = p
        self.normal = normal
        self.is_inside = False
        self.t = t


# Determine if ray hits inside or outside of Hittable
def front_face(ray_dir, outward_normal):
    if ray_dir.dot(outward_normal) > 0:
        normal = -outward_normal
        is_inside = True
    else:
        normal = outward_normal
        is_inside = False
    return normal, is_inside


# Abstract class for hittable objects like sphere, box etc.
class Hittable(ABC):
    def hit(self, r, t_min, t_max, hit_record):
        pass


class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max, hit_record):
        oc = r.origin - self.center
        a = r.dir.length_squared()
        half_b = oc.dot(r.dir)
        c = oc.length_squared() - self.radius ** 2
        discriminant = half_b * half_b - a * c

        if discriminant > 0:
            root = discriminant ** 0.5
            t = (-half_b - root) / a
            if t_max > t > t_min:
                incident_point = r.at(t)
                outward_normal = (incident_point - self.center) / self.radius
                normal, is_inside = front_face(r.dir, outward_normal)
                hit_record.p = incident_point
                hit_record.normal = normal
                hit_record.is_inside = is_inside
                hit_record.t = t
                return True  # incident_point, normal, t

            t = (-half_b + root) / a
            if t_max > t > t_min:
                incident_point = r.at(t)
                outward_normal = (incident_point - self.center) / self.radius
                normal, is_inside = front_face(r, outward_normal)
                hit_record.p = incident_point
                hit_record.normal = normal
                hit_record.is_inside = is_inside
                hit_record.t = t
                return True  # incident_point, normal, t

        return False
