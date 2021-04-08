/*
** EPITECH PROJECT, 2018
** my_compute_factorial_rec
** File description:
** 
*/

#include <stdio.h>

int my_compute_factorial_rec(int nb)
{
    int x = nb;

    if (x == 0) {
	return (0);
    }
    if (x == 1) {
	return (1);
    }
    if (x < 0) {
	return (1);
    }

    my_compute_factorial_rec(nb * (nb--));
    return (nb);
}

