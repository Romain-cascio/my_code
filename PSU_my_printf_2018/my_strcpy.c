/*
** EPITECH PROJECT, 2018
** my_strcpy
** File description:
** 
*/

char *my_strcpy(char *dest, char const *src)
{
    int x = 0;
    
    while (src[x] != '\0') {
	dest[x] = src[x];
	x = x + 1;
    }
    dest[x] = '\0';
    return (dest);
}
