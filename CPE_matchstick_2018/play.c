/*
** EPITECH PROJECT, 2019
** play.c
** File description:
** 
*/

#include <unistd.h>
#include <stdlib.h>
#include "my.h"

int detect(char **av, board_t *array)
{
    for (int x = 0; av[1][x] != '\0'; x++) {
        if (av[1][x] >= 48 && av[1][x] <= 57 && av[2][x] >= 48 && av[2][x] <= 57)
            return (0);
        return (1);
    }
}

char *get_next_line(int fd, board_t *array)
{
    array->test_D = 0;
    int size;
    char *buffer = malloc(sizeof(char) * READ_SIZE);
    char *str = malloc(sizeof(char) * READ_SIZE);
    int i = 0;

    while (buffer[0] != '\n') {
        if (read(fd, buffer, 1) == '\0') {
            array->test_D += 1;
            return (NULL);
        }
        if (buffer[0] != '\n')
            str[i] = buffer[0];
        i++;
    }
    return (str);
}

int valid_input(board_t *array)
{
    my_putstr("Your turn\n");
    my_putstr("Line:");
    array->new_ligne = my_getnbr(get_next_line(1, array));
    if (array->new_ligne <= array->max_lignes && array->new_ligne > 0)
        array->black_board[array->new_ligne - 1];
    else {
        my_putstr("Error: this line is out of range\n");
        return (1);
    }
    my_putstr("Matchs:");
    array->matchs = my_getnbr(get_next_line(1, array));
    if (array->matchs > array->max_matchsG) {
        my_printf("Error: you cannot remove more than %d matches per turn\n", array->max_matchsG);
        return (1);
    }
    if (array->matchs > array->black_board[array->new_ligne - 1]) {
        my_putstr("Error: not enough matches on this line\n");
        return (1);
    }
    if (array->matchs <= array->black_board[array->new_ligne - 1]) {
        array->black_board[array->new_ligne - 1] -= array->matchs;
        my_printf("Player removed %d match(es) from line %d\n", array->matchs, array->new_ligne);
    }
    return (0);
}

int check_end(board_t *array)
{
    int x = 0;
    int nbr = 0;

    for (int i = 0; i != array->max_lignes; i++) {
        while (x != array->black_board[i]) {
            if (x != 0)
                nbr++;
            x++;
        }
    }
    if (nbr != 0)
        return (1);
    return (0);
}