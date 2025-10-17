// Circle Drawing points
#include <stdio.h>
#include <stdlib.h>

void gp(int, int, int);
void plotPoints(int, int, int, int);

int main(int argc, char *argv[])
{
    if(argc != 4)
    {
        printf("Error\nUsage:\n\n%s <radius> <cx> <cy>", argv[0]);
        return -1;
    }

    int r = atoi(argv[1]);
    int cx = atoi(argv[2]), cy = atoi(argv[3]);

    gp(r, cx, cy);

    return 0;
}

void gp(int radius, int cx, int cy) {
    printf("[");
    int x = cx, y = cy + radius, p0 = 1 - radius;
    plotPoints(cx, cy, x, y);

    while (x < y) {
        x++;
        if(p0 < 0)
        {
            p0 = p0 + 2*x + 1;
        } else {
            y--;
            p0 = p0 + 2* (x - y) + 1;
        }
        plotPoints(cx, cy,  x, y);
    }
    printf("]");
}

void plotPoints(int cx, int cy, int x, int y)
{
    printf("(%d, %d),", cx + x, cy + y);
    printf("(%d, %d),", cx - x, cy + y);
    printf("(%d, %d),", cx + x, cy - y);
    printf("(%d, %d),", cx - x, cy - y);
    printf("(%d, %d),", cx + y, cy + x);
    printf("(%d, %d),", cx - y, cy + x);
    printf("(%d, %d),", cx + y, cy - x);
    printf("(%d, %d),", cx - y, cy - x);
}
