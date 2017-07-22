#include <stdio.h> 
#include <stdlib.h>
#include "set_operations.h"
#include "avl.h"

//creates a set
//returns a pointer to the set
set* create_set()
{
	set* S = (set*)malloc(sizeof(set));
	S->cardinality = 0;
	S->root = NULL;
	return S;
}

//add an element to the set
//input: set A to which the element is inserted, the element x to be inserted
void add_element(set* A, int x)
{	
	if(!is_present(A->root, x))
	{
		(A->cardinality)++;
		A->root = insert(A->root, x);
	}
}

//remove an element from the set
//input: set A from which the element is removed, the element x to be removed
void remove_element(set* A, int x)
{
	if(is_present(A->root, x))
	{
		(A->cardinality)--;
		A->root = delete(A->root, x);
	}
}

//check if a set is empty
//input: set A which should be checked for emptiness
//returns 1 if the set A is empty, 0 otherwise
int is_empty(set* A)
{	
	if(A->root == NULL)
		return 1;
	return 0;
}

//check if an element is present in the set
//input: set A in which the element is searched, the element x to be searched
//returns 1 if the element is present in set A, 0 otherwise
int is_present_set(set* A, int x)
{
	return is_present(A->root, x);
}

void union_inorder(node* T, set* S)
{
	if(T != NULL)
	{
		union_inorder(T->left, S);
		add_element(S, T->data);
		union_inorder(T->right, S);
	}
}
//find union of given two sets
//input: the wo sets A and B
//returns the pointer to the union of the sets A and B 
set* set_union(set* A, set* B)
{
	set* union_set = create_set();
	
	union_inorder(A->root, union_set);
	union_inorder(B->root, union_set);
	return union_set;
}

void intersection_inorder(node* T, set* B, set* S)
{
	if(T != NULL)
	{
		intersection_inorder(T->left, B, S);
		if(is_present_set(B, T->data))
			add_element(S, T->data);
		intersection_inorder(T->right, B, S);
	}
}
//find intersection of given two sets
//input: the wo sets A and B
//returns the pointer to the intersection of the sets A and B 
set* set_intersection(set* A, set* B)
{
	set* intersection_set = create_set();
	if(A->cardinality < B->cardinality)
	{
		intersection_inorder(A->root, B, intersection_set);
	}
	else
	{
		intersection_inorder(B->root, A, intersection_set);
	}
	return intersection_set;
}

void difference_inorder(node* T, set* B, set* S)
{
	if(T != NULL)
	{
		difference_inorder(T->left, B, S);
		if(!is_present_set(B, T->data))
			add_element(S, T->data);
		difference_inorder(T->right, B, S);
	}
}
//find difference of given two sets
//input: the wo sets A and B
//returns the pointer to the difference set A-B 
set* set_difference(set* A, set* B)
{
	set* difference_set = create_set();
	
	difference_inorder(A->root, B, difference_set);
	return difference_set;
}

//display all the elements of the set
//input: the set A whose elements are to be displayed
void display(set* A)
{
	inorder(A->root);
	printf("\n");
}
