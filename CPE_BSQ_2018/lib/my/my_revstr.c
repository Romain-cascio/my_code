/*
** EPITECH PROJECT, 2018
** my_revstr
** File description:
** 
*/

char *my_revstr(char *str)
{
    int x = 0;
    int y = 0;
    char swap;

    while   (str[x] != '\0') {
	x = x + 1;
    }
    x = x - 1;
    while (y < x) {
	swap = str[x];
        str[x] = str[y];
        str[y] = swap;
        x--;
        y++;
    }
    return (str);
}
