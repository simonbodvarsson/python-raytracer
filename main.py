import sys
import numpy as np
from vec3 import Vec3
from rich.progress import track

def write_color(pixel_color):
    print(str(int(255.999 * pixel_color.x)) + " " + \
          str(int(255.999 * pixel_color.y)) + " " + \
          str(int(255.999 * pixel_color.z)) + " ")

def main():
    image_width = 256
    image_height = 256

    print("P3")
    print(str(image_width) + " " + str(image_width) + "\n255")

    for j in track(range(image_height-1, -1, -1)):
        # print("Scanlines remaining: " + str(j), file=sys.stderr)
        for i in range(0, image_width):
            pixel_color = Vec3(float(i) / (image_width-1), float(j) / (image_height-1), 0.25)
            write_color(pixel_color)

            # print(str(ir) + " " + str(ig) + " " + str(ib))
    print("Done", file=sys.stderr)


if __name__ == '__main__':
    main()