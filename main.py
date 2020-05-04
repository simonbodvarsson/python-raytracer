import sys
import numpy as np
from vec3 import Vec3

def main():
    image_width = 256
    image_height = 256

    print("P3")
    print(str(image_width) + " " + str(image_width) + "\n255")

    for j in range(image_height-1, -1, -1):
        print("Scanlines remaining: " + str(j), file=sys.stderr)
        for i in range(0, image_width):
            r = float(i) / (image_width-1)
            g = float(j) / (image_height-1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(str(ir) + " " + str(ig) + " " + str(ib))
    print("Done", file=sys.stderr)


if __name__ == '__main__':
    main()