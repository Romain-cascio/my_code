/*
** EPITECH PROJECT, 2019
** all_stars.c
** File description:
** 
*/

#include "my.h"

void put_star(board_t *array)
{
    array->stars = (array->max_lignes - 1) * 2 + 3;

    for (int i = 0; i != array->stars; i++)
        my_putchar('*');
    my_putchar('\n');
}