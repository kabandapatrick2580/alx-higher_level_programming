#include "lists.h"
/**
 * cycle_detector - checks if a singly linked list has a cycle in it
 * @pointer_to_list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int cycle_detector(listint_t *pointer_to_list)
{
	listint_t *slow_traverse, *fast_traverse;

	if (pointer_to_list == NULL || pointer_to_list->next_node == NULL)
		return (0);

	slow_traverse = pointer_to_list;
	fast_traverse = pointer_to_list;

	while (fast_traverse != NULL && fast_traverse->next_node != NULL)
	{
		slow_traverse = slow_traverse->next_node;
		fast_traverse = fast_traverse->next_node->next_node;

		if (slow_traverse == fast_traverse)
			return (1);
	}

	return (0);
}
