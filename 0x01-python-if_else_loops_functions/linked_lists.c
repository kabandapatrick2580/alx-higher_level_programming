#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * print_custom_list - prints all elements of a custom_list_t list
 * @custom_head: pointer to head of custom_list_t list
 * Return: number of custom_nodes
 */
size_t print_custom_list(const custom_list_t *custom_head)
{
	const custom_list_t *custom_current;
	unsigned int custom_count; /* number of custom_nodes */

	custom_current = custom_head;
	custom_count = 0;
	while (custom_current != NULL)
	{
		printf("%i\n", custom_current->custom_value);
		custom_current = custom_current->custom_next;
		custom_count++;
	}

	return (custom_count);
}

/**
 * add_custom_node_end - adds a new custom_no
 * @custom_list_head: pointer to pointer of first cu
 * @custom_value: integer to be included in new cu
 * Return: address of the new custom_element or NULL i
 */
custom_list_t *add_custom_node_end(custom_list_t **custom_list_head,
		const int custom_value)
{
	custom_list_t *custom_new;
	custom_list_t *custom_current;

	custom_current = *custom_list_head;

	custom_new = malloc(sizeof(custom_list_t));
	if (custom_new == NULL)
		return (NULL);

	custom_new->custom_value = custom_value;
	custom_new->custom_next = NULL;

	if (*custom_list_head == NULL)
		*custom_list_head = custom_new;
	else
	{
		while (custom_current->custom_next != NULL)
			custom_current = custom_current->custom_next;
		custom_current->custom_next = custom_new;
	}

	return (custom_new);
}

/**
 * free_custom_list - frees a custom_list_t list
 * @custom_list_head: pointer to custom_list to be freed
 * Return: void
 */
void free_custom_list(custom_list_t *custom_list_head)
{
	custom_list_t *custom_current;

	while (custom_list_head != NULL)
	{
		custom_current = custom_list_head;
		custom_list_head = custom_list_head->custom_next;
		free(custom_current);
	}
}
