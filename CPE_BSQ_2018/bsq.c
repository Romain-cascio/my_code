/*
** EPITECH PROJECT, 2019
** CPE_BSQ_2018
** File description:
** bsq
*/

#include <sys/stat.h>
#include <stdlib.h>
#include "my.h"

int putchar_result(board_t *array)
{
    int x = 0;
    int y = 0;
    while (x != array->nb_line-1) {
        while (y != array->nb_cols) {
            my_putchar(array->black_board[x][y]);
            y++;
        }
        y = 0;
        x++;
        my_putchar('\n');
    }
}

int **sizeXY(board_t *array)
{
    int x = array->nb_line - array->map;
    int y = array->nb_cols - array->map;
    int saveY = array->nb_cols;
    while (array->nb_line != x) {
        while (array->nb_cols != y) {
            array->black_board[array->nb_line][array->nb_cols] = 120;
            array->nb_cols -= 1;
        }
        array->nb_cols = saveY;
        array->nb_line -= 1;
    }
    array->nb_line += array->map;
    array->nb_cols += array->map;
}

int rev_nbr_to_str(board_t *array)
{
    int line = -1;
    int col = -1;
    int z = 0;
    
    array->save_line = array->nb_line;
    array->save_col = array->nb_cols - 1;
    array->nb_line -= 1;
    array->nb_cols -= 1;
    while (array->nb_line != line) {
        while (array->nb_cols != col) {
            if (array->black_board[array->nb_line][array->nb_cols] == array->map && z == 0) {
                sizeXY(array);
                array->nb_cols = array->save_col;
                z++;
            }
            if (array->black_board[array->nb_line][array->nb_cols] > 0 &&
                array->black_board[array->nb_line][array->nb_cols] != 'x')
                array->black_board[array->nb_line][array->nb_cols] = '.';
            if (array->black_board[array->nb_line][array->nb_cols] < 1)
                array->black_board[array->nb_line][array->nb_cols] = 'o';
            array->nb_cols -= 1;
        }
        array->nb_line -= 1;
        array->nb_cols = array->save_col;
    }
    array->nb_line = array->save_line;
    array->nb_cols = array->save_col;
}

board_t *algoBSQ(board_t *array)
{
    int x = 1;
    int y = 1;
    array->map = 0;

    while (x != array->nb_line) {
        while (y != array->nb_cols) {
            if (array->black_board[x][y] > 0) {
                array->black_board[x][y] += smallnb(array->black_board[x][y - 1],
                array->black_board[x - 1][y], array->black_board[x - 1][y - 1], array);
                if (array->black_board[x][y] > array->map)
                    array->map = array->black_board[x][y];
            }
            y++;
        }
        x++;
        y = 1;
    }
    return (array);
}

int main(int ac, char** av)
{
    struct stat sb;
    board_t *array = malloc(sizeof(board_t)); 
    stat(av[1], &sb);
    all_in(av[1], sb.st_size, array);
    return (0);
}