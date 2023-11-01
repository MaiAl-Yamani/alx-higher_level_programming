#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - nserts a number into a sorted singly linked list
 * @head: pointer to pointer to head node
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		prev = *head;
		temp = (*head)->next;
		while (temp != NULL)
		{
			while (temp->n < new->n)
			{
				prev = temp;
				temp = temp->next;
			}
			new->next = temp;
			prev->next = new;
			return (new);
		}
		if (temp == NULL)
		{
			prev->next = new;
			return (new);
		}
	}
	return (NULL);
}
