#include"lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nouveau_node, *current;

	/* Create a new node */
	nouveau_node = malloc(sizeof(listint_t));
	if (nouveau_node == NULL)
		return (NULL);

	nouveau_node->n = number;
	nouveau_node->next = NULL;

	/* If the list is empty or the number < the head, insert at the beginning */
	if (*head == NULL || number < (*head)->n)
	{
		nouveau_node->next = *head;
		*head = nouveau_node;
		return (nouveau_node);
	}

	/* Traverse the list to find the appropriate position */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* Insert the new node in the middle or at the end of the list */
	nouveau_node->next = current->next;
	current->next = nouveau_node;

	return (nouveau_node);
}
