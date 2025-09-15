# CUDA
## What is CUDA?
- CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model developed by NVIDIA that allows developers to use NVIDIA GPUs for general-purpose computing (GPGPU).
- CUDA extends C/C++ with GPU specific keywords. It offloads the heavy work from CPU to GPU to leverage 1000s of parallel threads.
- CUDA is specifically for NVIDIA GPUs.

## CUDA Model
CUDA uses host-device model
	Host: The CPU and system memory (runs standard C/C++)
	Device: The GPU and it's memory (runs CUDA kernel code)

## Example of kernel code
```bash
__global__ void add(int *a, int *b, int *c) {
	int i = threadIdx.x;
	c[i] = a[i] + b[i];
}
```

## Some of the CUDA Libraries

- cuBLAS - GPU-accelerated BLAS (Basic Linear Algebra Subprograms), Mostly used for Matrix Multiplication, Vector Operations.
- cuFFT - Fast Fourier Transfrom library, Mostly used for Signal Processing and Spectral Analysis.
- cuSOLVER - Linear system solver, eigenvalue problems are the main focus of this library. Advanced math problems in science and engineering can be solved using this library.

## Examples of CUDA API functions
- cudaMalloc() - Allocates memory on the GPU.
- cudaMemcpy() - Transfers data between host and device.
- cudaFree() - Frees Device Memory
- cudaGetLastError() - Gets the last error from CUDA call

# OpenCL
## What is OpenCL?
- OpenCL is an open, royalty-free standard for parallel programming across hetrogeneous platforms including CPUs, GPUs, FPGAs and other processors.
- OpenCL is developed by **_The Khronos Group_**
- The goal of OpenCL is to create a portable code that runs on a variety of hardware from different vendors like NVIDIA, AMD, ARM etc.
- It is based on C99 for writting kernels, with APIs in C/C++/Java/Python

## OpenCL Model
OpenCL also uses a *Host-Device* model
- Host: The CPU, which manages the execution.
- Device: The compute device (GPU, CPU) that runs kernel code.

OpenCL defines three key concepts:
- Context: The environment for all OpenCL objects (devices, memory, command queues).
- Command Queue: Sends commands (kernel launches, memory copies) to devices.
- Program and Kernel: Program contain kernels, which runs on devices.

## some of the OpenCL API Functions
- clGetPlatformIDs() - Gets Available OpenCL platforms.
- clGetDeviceIDs() - Gets devices (GPU/CPU) from a platform.
- clCreateBuffer() - Allocates memory on device or shared memory.
- clBuildProgram() - Compiles the kernel program.

## Typical OpenCL Workflow
1. Discover platforms and devices
2. Create a context.
3. Create a command queue for the device.
4. Allocates device memory buffers.
5. Create and build a program from kernel source.
6. Create a kernel object from the program.
7. Set kernel arguments.
8. Enqueue the kernel for execution (specifying global & local work sizes).
9. Read back results from device memory.
10. Clean up resources.

## Example code for OpenCL
### OpenCL Vector Addition Example
```bash
const char* kernelSource = 
"__kernel void vacAdd(__global int* A, __global int* B, __global int* C) { int id = get_global_id(0);C[id] = A[id] + B[id]; }";
```

# OpenGL
## What is OpenGL?
- OpenGL is a cross-platform, cross-language API for rendering 2D and 3D graphics. It provides a set of functions to communicate with the GPU for hardware-accelerated graphics.
- OpenGL designed for real-time rendering like video games, CAD, visualization.
- OpenGL primarily uses C, but accessible for many languages.

## OpenGL Model
OpenGL is **immediate mode and state machine based**, meaning:
- You issue commands to set states.
- You define geometry (vertices) and how they should be drawn.
- The GPU processes these commands to render images.

## Some of the common OpenGL Functions
- glClearColor(r, g, b, a) - Sets the color used to clear the screen
- glClear(mask) - Clears buffers(color, depth, stencil).
- glEnable(cap) - Enables capabilities like depth test, blending.
- glGenBuffers(n, *buffers) - Generates buffer object names (IDs).

## Typical OpenGL Rendering Flow
1. Initialize OpenGL context.
2. Load and Compile shaders.
3. Create buffers and upload vertex data.
4. Set up vertex attributes (position, color, texture coords)
5. Clear Screen and set viewport.
6. Use shader program and bind buffers.
7. Draw geometry using `glDrawArrays` or `glDrawElements`.
8. Swap buffers to display rendered frame.

## Sample Code for OpenGL
### Vertex Shader (GLSL)
```glsl
// vertex_shader.glsl
#version 330 core
layout (location = 0) in vec3 aPos;     // Vertex position
layout (location = 1) in vec3 aColor;   // Vertex color

out vec3 vertexColor; // Output to fragment shader

void main()
{
    gl_Position = vec4(aPos, 1.0);
    vertexColor = aColor;
}
```

### Fragment Shader (GLSL)
```glsl
// fragment_shader.glsl
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
```
