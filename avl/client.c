#include <stdio.h>
#include "set_operations.h"

int main()
{
	set* A = create_set();
	set* B = create_set();
	set* union_set = NULL;
	set* intersection_set = NULL;
	set* difference_set = NULL;
	int num_a = 0;
	int num_b = 0;
	int element = 0;
	int i = 0;
	
	printf("Enter the number of elements of set A:\n");
	scanf("%d", &num_a);
	printf("Enter the elements of A:\n");
	for(i = 1; i <= num_a; i++)
	{
		scanf("%d", &element);
		add_element(A, element);
	}
	printf("Enter the number of elements of set B:\n");
	scanf("%d", &num_b);
	printf("Enter the elements of B:\n");
	for(i = 1; i <= num_b; i++)
	{
		scanf("%d", &element);
		add_element(B, element);
	}
	printf("Union of sets A and B\n");
	union_set = set_union(A, B);
	display(union_set);
	printf("Intersection of sets A and B\n");
	intersection_set = set_intersection(A, B);
	display(intersection_set);
	printf("Difference of set A and B\n");
	difference_set = set_difference(A, B);
	display(difference_set);
	
	return 0;
}
