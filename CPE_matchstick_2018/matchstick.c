/*
** EPITECH PROJECT, 2019
** matchstick.c
** File description:
** 
*/

#include <stdlib.h>
#include "my.h"

int *count_size(int ac, char **av, board_t *array)
{
    array->max_lignes = my_getnbr(av[1]);
    array->max_matchsG = my_getnbr(av[2]);
    array->black_board = malloc(sizeof(board_t) * (array->max_lignes + 1));

    for (int x = 0; x != array->max_lignes; x++) {
        array->black_board[x] = x * 2 + 1;
    }
    return (array->black_board);
}

int *print_map(board_t *array)
{
    int space;

    put_star(array);
    for (int i = 0; i != array->max_lignes; i++) {
        space = (array->last_line - (i * 2)) / 2;
        my_putchar('*');
        for (int SP = 0; SP != space; SP++)
            my_putchar(' ');
        for (int x = 0; x != array->black_board[i]; x++)
            my_putchar('|');
        for (int SP = 0; SP != array->last_line - array->black_board[i] - space; SP++)
            my_putchar(' ');
        my_putchar('*');
        my_putchar('\n');
    }
    put_star(array);
    my_putchar('\n');

    return (array->black_board);
}

int play(int ac, char **av, board_t *array)
{
    while (1) {
        print_map(array);
        while (valid_input(array) == 1)
            print_map(array);
        if (array->test_D > 0) {
            break;
            return (3);
        }
        print_map(array);
        generate_IA(array);
        if (check_end(array) == 0) {
            my_putstr("I lost... snif...but I'll get you next time\n");
            return (0);
        }
    }
}
int main(int ac, char **av, board_t *array)
{
    if (detect(av, array) == 0) {
        array->max_lignes = my_getnbr(av[1]);
        array->last_line = (array->max_lignes - 1) * 2 + 1;
        array->black_board = count_size(ac, av, array);
        if (play(ac, av, array) == 3)
        return (0);
    }
    else
        return (84);

    return (0);
}