#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a listint_t type singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list->flag == 1)
			return (1);

		list->flag = 1;
		list = list->next;
	}

	return (0);
}
