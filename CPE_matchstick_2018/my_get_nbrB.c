/*
** EPITECH PROJECT, 2018
** my_get_nbr
** File description:
** 
*/

#include "my.h"

/*void my_putchar(char c)
{
    write(1, &c, 1);
}*/

int my_getnbr(char const *str)
{
	int x = 0;
	int result = 0;

	while (str[x] != '\0') {
		if (str[x] < 48 || str[x] > 57)
			x++;
		if (str[x] >= 48 && str[x] <= 57) {
			if (str[x - 1] == '-') {
				my_putchar('-');
			}
			result *= 10;
			result += (str[x] - 48);
			x++;
		}
	}
	return (result);
}
