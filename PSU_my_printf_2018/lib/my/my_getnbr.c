/*
** EPITECH PROJECT, 2018
** my_getnbr
** File description:
** 
*/

#include <stdio.h>

int my_getnbr(char const *str)
{
    int x;
    int y = -1;
    int z;

    while (str[x] < 48 || str[x] > 57) {
	x = x + 1;
    }
    if (y < 0) {
	x = x * -1;
    }
    while (str[x] >= 48 && str[x] <= 57) {
	return(x);
    }
    if (x > 48 && x < 57) {
	x = x + 48;
    }
    return (x);
}

int main()
{
    printf("&d\n",my_getnbr("59"));
    return (0);
}
	
