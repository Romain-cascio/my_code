/*
** EPITECH PROJECT, 2018
** my_ptrintf
** File description:
** 
*/

#include <stdlib.h>
#include <stdarg.h>
#include "my.h"

int my_putstrlen(char* str)
{
    int i = 0;
    int nbs = 0;
    
    while (str[i] != '\0') {
	my_putchar(str[i]);
	i++;
	nbs++;
    }
    return(nbs);
}

int works(int flag, va_list ap)
{
    int nb = 0;

    if (flag == 's') {
	nb = my_putstrlen(va_arg(ap, char*));
    }
    if (flag == 'd') {
        nb = my_put_nbr(va_arg(ap, int));
    }
    if (flag == 'c') {
        nb = my_putstrlen(va_arg(ap, char*));
    }
    va_end(ap);
    return(nb);
}

int works2(int flag, va_list ap)
{
    int nb = 0;
    
    if (flag == 'x') {
        nb = my_putnbr_base(va_arg(ap, int),"0123456789ABCDEF");
    }
    if (flag == 'b') {
        nb = my_putnbr_base(va_arg(ap, int),"01");
    }
    if (flag == 'o') {
        nb = my_putnbr_base(va_arg(ap, int),"01234567");
    }
    va_end(ap);
    return(nb);
}

int my_printf(char *blyat, ...)
{
    int i = 0;
    int flag;
    va_list ap;


    int nb = 0;
    
    va_start(ap, blyat);
    while (blyat[i] != '\0') {
	if (blyat[i] != '%') {
	my_putchar(blyat[i]);
	nb++;
	}
	if (blyat[i] == '%') {
	    flag = blyat[i + 1];

	    nb = nb + works(flag,ap);
       nb = nb + works2(flag, ap);
	    i = i + 1;
	}
	i++;
    }
    return(nb);
}
