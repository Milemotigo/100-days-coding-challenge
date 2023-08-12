#include <stdio.h>

int main() {

        int a[] = {1, 3, 4, 7, 9, 2, 6};
        int n = sizeof(a) / sizeof(a[0]);
        printf("%d\n", n);
	printf ("%lu\n %lu\n", sizeof(a), sizeof(a[0]));
}
