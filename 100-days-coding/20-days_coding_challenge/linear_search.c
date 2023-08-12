#include<stdio.h>

int main(void)
{
	int a, i, n, d;
	a = {1, 2, 5, 6, 7};
	n = a[4];
	for(i = 0; i < n; i++)
	{
		if (a[i] == n)
		{
			printf("element found at index", i);
		}
		break;
	}
	if (i == n)
		printf("elemeng not found");
}
