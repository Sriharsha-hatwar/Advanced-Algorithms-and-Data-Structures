#ifndef AVL_H
#define AVL_H

typedef struct node
{
	int data;
	struct node* left;
	struct node* right;
	int ht;
} node;

node* insert(node*, int);
node* delete(node*, int);
void preorder(node*);
void inorder(node*);
int height(node*);
node* rotateright(node*);
node* rotateleft(node*);
node* RR(node*);
node* LL(node*);
node* LR(node*);
node* RL(node*);
int BF(node*);
int is_present(node*, int);

#endif
