#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	int i;

	head = NULL;
	add_nodeit(&head, 0);
	add_nodeit(&head, 1);
	add_nodeit(&head, 2);
	add_nodeit(&head, 3);
	add_nodeit(&head, 4);
	add_nodeit(&head, 98);
	add_nodeit(&head, 402);
	add_nodeit(&head, 1024);
	print_listint(head);

	if (cycle_detector(head) == 0)
		printf("Linked list has no cycle\n");
	else if (cycle_detector(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next_node;
	temp = current->next_node;
	current->next_node = head;

	if (cycle_detector(head) == 0)
		printf("Linked list has no cycle\n");
	else if (cycle_detector(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next_node;
	current->next_node = temp;

	free_listint(head);

	return (0);
}
