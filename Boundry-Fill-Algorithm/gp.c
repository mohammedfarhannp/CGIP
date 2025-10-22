#include <stdio.h>
#include <stdlib.h>

#define SIDE 2048

int canvas[SIDE][SIDE];

void set_pixel(int, int, int);
void draw_line(int, int, int, int);
void boundary_fill(int, int, int, int);
void bresenhams(int, int, int, int);
void getSeedPoint(int[], int[], int, int*, int*);

int main(int argc, char* argv[])
{
    if(argc < 2 || (argc - 1) % 2 != 0)
    {
        printf("Usage:\n%s <x1> <y1> <x2> <y2>.....\n", argv[0]);
        return 1;
    }

    int n = (argc - 1) / 2;
    int x[n], y[n];
    int i, j = 0;

    for (i = 1; i < argc; i++)
    {
        if (i % 2 != 0)
            x[j] = atoi(argv[i]);
        else
            y[j++] = atoi(argv[i]);
    }


    printf("{(");
    for(i = 0; i < n; i++)
    {
        int next = (i + 1) % n;
        printf("(");
        bresenhams(x[i], y[i], x[next], y[next]);
        printf("), ");
    }
    printf(")");

    for (int y = 0; y < SIDE; y++)
        for (int x = 0; x < SIDE; x++)
            canvas[y][x] = 0;

    for (int i  = 0; i < n; i++)
    {
        int next = (i + 1) % n;
        draw_line(x[i], y[i], x[next], y[next]);
    }

    int seed_x, seed_y;

    getSeedPoint(x, y, n, &seed_x, &seed_y);

    printf(":(");
    boundary_fill(seed_x, seed_y, 2, 1);
    printf(")}");
    return 0;
}

void getSeedPoint(int polyX[], int polyY[], int n, int *seedX, int *seedY) {
    int sumX = 0, sumY = 0;
    for (int i = 0; i < n; i++) {
        sumX += polyX[i];
        sumY += polyY[i];
    }
    *seedX = sumX / n;
    *seedY = sumY / n;
}

void boundary_fill(int x, int y, int fill_color, int boundary_color) {
    if (x < 0 || x >= SIDE || y < 0 || y >= SIDE)
        return;

    if(canvas[y][x] != boundary_color && canvas[y][x] != fill_color) {
        canvas[y][x] = fill_color;
        printf("(%d, %d),", x, y);
        boundary_fill(x + 1, y, fill_color, boundary_color);
        boundary_fill(x - 1, y, fill_color, boundary_color);
        boundary_fill(x, y + 1, fill_color, boundary_color);
        boundary_fill(x, y - 1, fill_color, boundary_color);
    }
}

void draw_line(int x0, int y0, int x1, int y1)
{
    int dx = abs(x1 - x0), dy = abs(y1 - y0);
    int sx = x0 < x1 ? 1 : -1, sy = y0 < y1 ? 1 : -1;
    int err = dx - dy;

    while (1) {
        set_pixel(x0, y0, 1);

        if(x0 == x1 && y0 == y1)
            break;

        int e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x0 += sx;
        }

        if (e2 < dx) {
            err += dx;
            y0 += sy;
        }
    }
}

void set_pixel(int x, int y, int val)
{
    if(x >= 0 && x < SIDE && y >= 0 && y < SIDE)
        canvas[y][x] = val;
}

void bresenhams(int x1, int y1, int x2, int y2)
{
    int dx, dy, sx, sy, err;

    dx = abs(x2 - x1);
    dy = abs(y2 - y1);

    sx = x1 < x2 ? 1 : -1;
    sy = y1 < y2 ? 1 : -1;

    err = dx - dy;

    while (1)
    {
        printf("(%d, %d),", x1, y1);

        if (x1 == x2 && y1 == y2) break;

        int e2 = 2 * err;

        if(e2 > -dy)
        {
            err -= dy;
            x1 += sx;
        }

        if(e2 < dx)
        {
            err += dx;
            y1 += sy;
        }
    }
}