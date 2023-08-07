#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * printit - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t printit(const listint_t *h)
{
	const listint_t *current;
	unsigned int intgr; /* number of nodes */

	current = h;
	intgr = 0;
	while (current != NULL)
	{
		printf("%i\n", current->intgr);
		current = current->next_node;
		intgr++;
	}

	return (intgr);
}

/**
 * add_nodeit - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @intgr: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeit(listint_t **head, const int intgr)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->intgr = intgr;
	new->next_node = *head;
	*head = new;

	return (new);
}

/**
 * free_it - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_it(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next_node;
		free(current);
	}
}
