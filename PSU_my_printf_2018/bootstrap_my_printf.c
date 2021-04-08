/*
** EPITECH PROJECT, 2018
** my_printf_bootstrap
** File description:
** 
*/
int argnb(int space);
{
    int i = 0;

    while (i != '\0') {
	i++;
	if (i == ' ') {
	    space++;
	}
    }
}

int sum_stdarg(int i, int nb, ...)
{
    if (i == 0) {
	nb = argnb;
	return(nb);
    }
    if (i == 1) {
	nb = my_strlen(str);
	my_strlen(str);
	return(nb);
    }
}
int disp_stdarg(char *s, ...);
{
    int i = 0;
    
    while (i != '\0') {
	if (i == '\n') {
	    
}
