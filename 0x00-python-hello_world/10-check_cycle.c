#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function to check if the linked list has a cycle
 * @list: the list
 * Return: one if it is cycle zero if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;
	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return 1;
	}

    return 0;
}
