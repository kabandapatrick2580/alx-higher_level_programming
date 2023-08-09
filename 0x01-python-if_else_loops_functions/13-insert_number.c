#include "custom_lists.h"
#include <stdlib.h>

/**
 * custom_insert_node - Inserts a value into a sorted singly custom_linked_list.
 * @custom_head: Pointer to the head of the custom_linked_list.
 * @custom_value: Value to be inserted.
 *
 * Return: The address of the new custom_node, or NULL if it failed.
 */
custom_list_t *custom_insert_node(custom_list_t **custom_head, int custom_value)
{
	custom_list_t *custom_new_node, *custom_current;

	/* Create a new custom_node */
	custom_new_node = malloc(sizeof(custom_list_t));
	if (custom_new_node == NULL)
		return (NULL);

	custom_new_node->custom_value = custom_value;
	custom_new_node->custom_next = NULL;

	/* If the custom_linked_list is empty or the custom_value < the custom_head, insert at the beginning */
	if (*custom_head == NULL || custom_value < (*custom_head)->custom_value)
	{
		custom_new_node->custom_next = *custom_head;
		*custom_head = custom_new_node;
		return custom_new_node;
	}

	/* Traverse the custom_linked_list to find the appropriate position */
	custom_current = *custom_head;
	while (custom_current->custom_next != NULL && custom_current->custom_next->custom_value < custom_value)
		custom_current = custom_current->custom_next;

	/* Insert the new custom_node in the middle or at the end of the custom_linked_list */
	custom_new_node->custom_next = custom_current->custom_next;
	custom_current->custom_next = custom_new_node;

	return custom_new_node;
}

