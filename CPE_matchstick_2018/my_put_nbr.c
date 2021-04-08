/*
** EPITECH PROJECT, 2018
** my_put_nbr
** File description:
** 
*/

#include <unistd.h>
#include "my.h"

int my_put_nbr (int nb)
{
    if ( nb == -2147483648 ) {
	my_putchar('-');
	my_putchar('2');
	my_put_nbr(147483648);
	return (0);
    }
    if	( nb < 0 ) {
        nb = nb * -1;
	my_putchar('-');
	my_put_nbr(nb);
	return (0);
    }	

    if	( nb <= 9 ) {
	my_putchar( nb + 48 );
	return (0);
    }

    my_put_nbr( nb / 10 );
    my_put_nbr( nb % 10 );
    return (0);
}
