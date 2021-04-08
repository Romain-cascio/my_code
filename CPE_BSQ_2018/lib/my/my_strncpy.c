/*
** EPITECH PROJECT, 2018
** my_strncpy
** File description:
** 
*/

#include <string.h>

char *my_strncpy(char *dest, char const *src, int n)
{
    int x = 0;

    while (src[x] != '\0' && x < n) {
	dest[x] = src[x];
	    x++;
    }
    if (x < n) {
	dest[x] = '\0';
    }
    return (dest);
    
}
		
