#include <stdio.h>
#include <stdlib.h>

void bresenhams(int, int, int, int);

int main(int argc, char* argv[])
{
    if(argc != 5)
    {
        printf("Usage:\n%s <x1> <y1> <x2> <y2>", argv[0]);
        return 1;
    }

    bresenhams(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]), atoi(argv[4]));

    return 0;
}

void bresenhams(int x1, int y1, int x2, int y2)
{
    int dx, dy, sx, sy, err;

    dx = abs(x2 - x1);
    dy = abs(y2 - y1);

    sx = x1 < x2 ? 1 : -1;
    sy = y1 < y2 ? 1 : -1;

    err = dx - dy;

    printf("[");
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
    printf("]");
}