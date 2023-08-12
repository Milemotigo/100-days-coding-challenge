#include <stdio.h>
#include <math.h>

int main()
{

	int i, b;
	float size;


	int a[] = {1, 3, 5, 6, 8};
	size = sizeof(a) / sizeof(a[0]);
	b = sqrt(size);
	for (i = 0; i <= b; i++)
	{
		printf("%d\n", a[i]);
	}
	return (0);
}
