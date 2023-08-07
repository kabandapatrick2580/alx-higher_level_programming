#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @intgr: integer
 * @next_node: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int intgr;
	struct listint_s *next_node;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int intgr);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

