#include "set.h"
#ifndef SET_OPERATIONS_H
#define SET_OPERATIONS_H

set* create_set();
void add_element(set* A, int x);
void remove_element(set* A, int x);
int is_empty(set* A);
int is_present_set(set* A, int x);
set* set_union(set* A, set* B);
set* set_intersection(set* A, set* B);
set* set_difference(set* A, set* B);
void display(set* A);
 
#endif
