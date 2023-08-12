#include <stdio.h>
#include <stddef.h>

int linear_search(int *array, size_t size, int value)
{
	size_t n;
	for (n = 0; n < size; n++){
		printf("Value checked array [%lu] = [%d]\n", n, array[n]);

		if (array[n] == value) {
			return n;
		}
		if (array == NULL)
		{
			return (-1);
		}
	}
	return (-1);
}
