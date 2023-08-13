#include "lists.h"

/**
 * reverse_listint - reverses linked list
 * @head: head of node
 *
 * Return: first node of the reversed linked list
 */
int is_palindrome(listint_t **new_head)
{
    listint_t *current_ptr;
    listint_t *previous_ptr;

    if (*new_head == NULL)
    {
        return (1);
    }
    previous_ptr = (*new_head)->next;
    (*new_head)->next = NULL;

    while (previous_ptr != NULL)
    {
        current_ptr = previous_ptr->next;
        previous_ptr->next = *new_head;

        *new_head = previous_ptr;
        previous_ptr = current_ptr;
    }
    return (0);
}
