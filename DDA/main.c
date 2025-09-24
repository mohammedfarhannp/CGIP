// C Code for calculating all points between point A and point B
// Compilation : gcc main.c -o main | gcc main.c -o main.exe
// Execution : ./main 20 20 40 40 | .\main.exe 20 20 40 40
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct point {
    int x;
    int y;
};

void get_points(struct point, struct point);

int main(int argc, char *argv[])
{
    if(argc != 5)
    {
        printf("Not Enough Arguments!\nUsage: %s <x1> <y1> <x2> <y2>");
        return -1;
    }
    
    struct point p1, p2;

    p1.x = atoi(argv[1]);
    p1.y = atoi(argv[2]);

    p2.x = atoi(argv[3]);
    p2.y = atoi(argv[4]);

    get_points(p1, p2);
    return 0;
}

void get_points(struct point A, struct point B)
{
    float dx = B.x - A.x;
    float dy = B.y - A.y;

    float steps = fabs(dx) > fabs(dy) ? fabs(dx) : fabs(dy);

    float x_inc = dx / steps;
    float y_inc = dy / steps;

    float x = A.x;
    float y = A.y;
    printf("[");
    for(int i = 0; i <= steps; i++)
    {
        printf("(%d, %d)", (int) x, (int) y);
        x += x_inc;
        y += y_inc;
        if(i < steps)
            printf(",");
    }
    printf("]");
}
