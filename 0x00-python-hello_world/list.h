#ifndef LIST_H
#define LIST_H

#include <stdlib.h>
/**
 * struct listint_s - is a variable
 * @n : is a integer
 * @next : a varaible
 * listint_t - is also a variable
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_s;

int check_cycle(listint_t *list);
#endif
