#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal_helper(head, *head));
}
/**
 * check_pal_helper - checks if a list is palindrome
 * @head: pointer to the beginning of the list
 * @last: pointer to the end of the list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int check_pal_helper(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal_helper(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
