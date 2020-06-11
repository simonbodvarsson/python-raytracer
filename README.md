# python-raytracer
A ray tracer written in Python based on this [C++ tutorial](https://raytracing.github.io/books/RayTracingInOneWeekend.html).   

![Randomly generated scene of spheres.](./example.png?raw=true "Output")

A randomly generated scene of spheres of different materials: diffuse, glass and metal.

## Objective:
Write a simple ray tracer in Python which can be improved and expanded upon.

**Current Status**
- Simple unit tested ray tracer.
- One type of hittable object: Sphere.
- Three different materials: Diffuse, Glass and Metal.
- Anti-aliasing via sub-pixel sampling.
- Positionable Camera.
- Defocus Blur (aka. Depth of Field).
- Randomly generated scene of spheres.
- Parallelized with multiprocessing.

**Next Steps**
- Output intermediate results.
- Add more object types.
- Add lights.
- Add textures.

**Possible stretch goals**
- Add DLSS (Deep Learning Super Sampling)
- Add compilation to CUDA via Numba.
- Add UI to view output
- Add input config to UI
- Allow for adjusting viewpoint in real time.
- Support different textures: Glossy, matte etc.
- Planet/Terrain procedural generation

**Test Coverage**

Unit Test coverage is currently at 61%. This is neglected for now to develop faster.

To discover and run all unit tests: `coverage run -m unittest discover`

To generate HTML test report: `coverage html`

