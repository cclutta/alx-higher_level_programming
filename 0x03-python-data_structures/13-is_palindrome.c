#include "lists.h"

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: listint_t node
*
* Return: 1 or 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *new = *head;
	int t[1024];
	int i = 0;
	int j = 0;
	
	if (*head)
	{
		while (new)
		{
			t[i] = new->n;
			new = new->next;
			i++;
		}
		
		while (j < i / 2)
		{
			if (t[j] == t[i - j - i])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
