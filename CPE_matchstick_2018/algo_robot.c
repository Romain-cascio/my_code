/*
** EPITECH PROJECT, 2019
** all_stars.c
** File description:
** 
*/

#include "my.h"

void generate_IA(board_t *array)
{
    int x = 0;

    my_putstr("AI's turn...\n");
    while (array->black_board[x] == 0) {
        x++;
    }
    array->black_board[x] -= 1;
    my_printf("AI's remove 1 match(es) from line %d\n", array->black_board[x]);
}