#include <stdio.h>
#include <stdlib.h>
#include "avl.h"
static int rotation = 0;//to restrict one rotation per one insertion|deletion

//insert a node into the avl tree recursively
//input: a node T of the tree, value x to be inserted
//returns the root of the subtree where insertion is done
node* insert_node(node* T, int x)
{
	//if the node T is null create a new node 
	if(T == NULL)
    {
    	T = (node*)malloc(sizeof(node));
		T->data = x;
		T->left = NULL;
		T->right = NULL;
	}
	//if the value x is greater than the value at node T
	else if(x > T->data)
    {
    	//insert to the right of T
		T->right = insert(T->right, x);
		//if the node T gets unbalanced, balance accordingly
		if(rotation != 1 && BF(T) == -2)
		{
			if(x > T->right->data)
				T = RR(T);
			else
		 		T = RL(T);
		}
	}
	//if the value x is less than the value at node T
	else if(x < T->data)
	{
		//insert to the left of T
		T->left = insert(T->left, x);
		//if the node T gets unbalanced, balance accordingly
		if(rotation != 1 && BF(T) == 2)
		{
			if(x < T->left->data)
				T = LL(T);
			else
				T = LR(T);
		}
	}
	//calculate the height of T after insertion
	T->ht = height(T);
	return T;
}
//a wraper function of insert_node() to reassign the value of the variable rotation
//input: the root T of the tree, value x to be inserted
//returns the root of the tree
node* insert(node* T, int x)
{
	rotation = 0;
	return insert_node(T, x);
}

//delete a node from the avl tree recursively
//input: a node T of the tree, value x to be deleted
//returns the root of the tree where the deletion is done
node* delete_node(node* T, int x)
{
	node* p;
	//if the node T is null, return null
	if(T == NULL)
	{
		return NULL;
	}
	//if the value x to be deleted is greater than the value at the node T
	else if(x > T->data)
	{
		//delete from the right subtree of T
		T->right = delete(T->right, x);
		//if T gets unbalanced after deletion, balance accordingly
		if(rotation != 1 && BF(T) == 2)
		{
			if(BF(T->left) >= 0)
				T = LL(T);
			else
				T = LR(T);
		}
	}
	//if the value x to be deleted is less than the value at the node T
	else if(x < T->data)
	{
		//delete from the left subtree of T
		T->left = delete(T->left, x);
		//if T gets unbalanced after deletion, balance accordingly
		if(rotation != 1 && BF(T) == -2)
		{
			if(BF(T->right) <= 0)
				T = RR(T);
			else
				T = RL(T);
		}
	}
	//if the value x to be deleted is equal to the value at node T, delete T
	else
	{
		//if the node T has right subtree
		if(T->right != NULL)
		{
			//replace T with its inorder successor
			p = T->right;
			while(p->left != NULL)
				p = p->left;
			T->data = p->data;
			//delete the inorder successor of T recursively
			T->right = delete(T->right, p->data);
			//if T gets unbalanced after deletion, balance accordingly
			if(rotation != 1 && BF(T) == 2)
			{
				if(BF(T->left) >= 0)
					T = LL(T);
				else
					T = LR(T);
			}
		}
		else return T->left;
	}
	//calculate the height of T after deletion
	T->ht = height(T);
	return T;
}
//a wraper function of delete_node() to reassign the value of the variable rotation
//input: the root T of the tree, value x to be deleted
//returns the root of the tree
node* delete(node* T, int x)
{
	rotation = 0;
	return delete_node(T, x);
}

//calculate the height of a node recursively
//input: node T whose height is to be calculated
//returns the height of T
int height(node* T)
{
	int lh;
	int rh;
	if(T == NULL)
		return 0;
	if(T->left == NULL)
		lh = 0;
	else
		lh = 1 + T->left->ht;
	if(T->right == NULL)
		rh = 0;
	else
		rh = 1 + T->right->ht;
	if(lh > rh)
		return lh;
	return rh;
}

//perform right rotation
//input: the unbalanced node x
//returns the root of the subtree after the rotation
node* rotateright(node* x)
{
	node* y;
	y = x->left;
	x->left = y->right;
	y->right = x;
	x->ht = height(x);
	y->ht = height(y);
	return y;
}

//perform left rotation
//input: the unbalanced node x
//returns the root of the subtree after the rotation
node* rotateleft(node* x)
{
	node* y;
	y = x->right;
	x->right = y->left;
	y->left = x;
	x->ht = height(x);
	y->ht = height(y);
	return y;
}

//perform R rotation
//input: the unbalanced node T
//returns the root of the tree of after rotation
node* RR(node* T)
{
	T = rotateleft(T);
	rotation = 1;
	return T;
}

//perform L rotation
//input: the unbalanced node T
//returns the root of the tree of after rotation
node* LL(node* T)
{
	T = rotateright(T);
	rotation = 1;
	return T;
}

//perform LR rotation
//input: the unbalanced node T
//returns the root of the tree of after rotation
node* LR(node* T)
{
	T->left = rotateleft(T->left);
	T = rotateright(T);
	return T;
}

//perform RL rotation
//input: the unbalanced node T
//returns the root of the tree of after rotation
node* RL(node* T)
{
	T->right = rotateright(T->right);
	T = rotateleft(T);
	return T;
}

//calculate the balanced factor of the given node
//input: node T whose balanced factor is to be calculated
//reuturns the balanced factor of T
int BF(node* T)
{
	int lh;
	int rh;
	if(T == NULL)
		return 0;
	if(T->left == NULL)
		lh = 0;
	else
		lh = 1 + T->left->ht;
	if(T->right == NULL)
		rh = 0;
	else
		rh = 1 + T->right->ht;
	return lh - rh;
}

//check if a value is present in the tree
//input: root T of the tree, value x to be inserted
//returns 1 if x is present in the tree, 0 otherwise
int is_present(node* T, int x)
{
	if(T != NULL)
	{
		if(x > T->data)
			return is_present(T->right, x);
		else if(x < T->data)
			return is_present(T->left, x);
		else if(x == T->data)
			return 1;
		return 0;
	}
	return 0;
}

//preorder traversal
void preorder(node* T)
{
	if(T != NULL)
	{
		printf("%d(BF = %d)\t", T->data, BF(T));
		preorder(T->left);
		preorder(T->right);
	}
}

//inorder traversal
void inorder(node* T)
{
	if(T != NULL)
	{
		inorder(T->left);
		printf("%d (BF = %d) ", T->data, BF(T));
		inorder(T->right);
	}
}

