#include "lists.h"

/**
 * check_cycle - hecks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: int 
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;
	
	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		
		if (a == b)
			return (1);
	}
	return (0);
}
