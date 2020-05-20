from hittable import HitRecord


class HittableList:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def clear(self):
        self.objects = []

    def hit(self, r, t_min, t_max, hit_record):
        hit_anything = False
        closest_so_far = t_max

        temp_rec = HitRecord(None, None, None)
        for obj in self.objects:
            if obj.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                hit_record.p = temp_rec.p
                hit_record.normal = temp_rec.normal
                hit_record.is_inside = temp_rec.is_inside
                hit_record.t = temp_rec.t
        return hit_anything
