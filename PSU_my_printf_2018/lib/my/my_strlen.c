/*
** EPITECH PROJECT, 2018
** my_strlen
** File description:
** 
*/

int my_strlen (char const *str)
{
    int x;
    x = 0;

    while   (str[x] != '\0') {
	x = x + 1;
    }
    return (x);
}
