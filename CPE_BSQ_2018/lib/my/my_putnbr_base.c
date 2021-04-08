/*
** EPITECH PROJECT, 2018
** my_putnbr_base
** File description:
** 
*/

int my_putnbr_base(int nbr, char const *base)
{
    int nb = 0;
    int len = my_strlen(base);
    
    nb = nbr % len;
    nbr = nbr / len;
    if (nbr > 0) {
	my_putnbr_base(nbr, base);
	my_putchar(base[nb]);
    }
    if (nbr == 0) {
    my_putchar(base[nb]);
    }
}
