#include <stdio.h>
#include <stdlib.h>
#include "avl.h"

int main()
{
	node* root = NULL;
	int x;
	int n;
	int i;
	int op;
	do
	{
		printf("1>Create:\n");
		printf("2>Insert:\n");
		printf("3>Delete:\n");
		printf("4>Print:\n");
		printf("5>check if present:\n");
		printf("6>Quit:\n");
		printf("Enter Your Choice:\n");
		scanf("%d", &op);
		switch(op)
		{
			case 1:printf("Enter no. of elements:\n");
					scanf("%d", &n);
					printf("Enter tree data:\n");
					root = NULL;
					for(i = 0; i < n; i++)
					{
						scanf("%d", &x);
						root = insert(root, x);
					}
					break;
			case 2:printf("Enter a data:\n");
					scanf("%d", &x);
					root = insert(root, x);
					break;
			case 3:printf("Enter a data:\n");
					scanf("%d", &x);
					root = delete(root, x);
					break;
			case 4:printf("Preorder sequence: ");
					preorder(root);
					printf("\n");
					printf("Inorder sequence: ");
					inorder(root);
					printf("\n");
					break;
			case 5:printf("Enter the element: ");
					scanf("%d", &x);
					int a = is_present(root, x);
					if(a == 1)
						printf("present");
		}
	}while(op!=6);
	return 0;
}

