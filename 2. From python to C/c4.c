/* prints max and min values in from input values 
   each in a separate line. After input numbers, 
   Use CTRL+D to start*/
#include <stdio.h>
int main() {
    int first = 1;
    int val, maxval, minval;

    while(scanf("%d", &val) != EOF) {
        if ( first || val > maxval) maxval = val;
        if ( first || val < minval) minval = val;
        first = 0;
    }

    printf("Maximum %d\n", maxval);
    printf("Minimum %d\n", minval);
}