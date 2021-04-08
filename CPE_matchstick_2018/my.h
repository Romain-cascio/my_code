/*
** EPITECH PROJECT, 2018
** my.h
** File description:
** 
*/

#include <SFML/Graphics.h>

typedef struct
{
    int *black_board;
    int max_lignes;
    int new_ligne;
    int last_line;
    int matchs;
    int stars;
    int max_matchsG;
    int IA_ligne;
    int IA_matchs;
    int test_D;
}board_t;

void my_putchar(char c);
char my_putstr(char* str);
int my_getnbr(char const *str);
int valid_input(board_t *array);
void put_star(board_t *array);
int check_end(board_t *array);
void generate_IA(board_t *array);
int detect(char** av, board_t *array);
int my_printf(char *blyat, ...);
int my_put_nbr (int nb);
int my_putnbr_base(int nbr, char const *base);
int my_strlen (char const *str);
char *get_next_line(int fd, board_t *array);

#ifndef READ_SIZE
#define READ_SIZE (1)
#endif