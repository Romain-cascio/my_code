/*
** EPITECH PROJECT, 2018
** my_str_to_word_array
** File description:
** 
*/

#include <unistd.h>
#include <stdlib.h>

int my_show_word_array(char * const *tab);

int detect(char x)
{
    if (x >= 65	&& x <= 90 || x >= 97 && x <= 122 || x >= 48 && x <= 57)
	return (1);
    return (0);
}

int count_words(char const *str)
{
    int x = 0;
    int count;
    
    while (str[x] != '\0') {
	x++;
	if (detect(str[x])) {
	    count++;
	}
	
    }
    return (count);
}
int count_char(char const *str)
{
    int i = 0;
    
    while (detect(str[i])) {
	i++;
    }
    return (i);
}

char **my_str_to_word_array(char const *str)
{
    int x = 0;
    int y = 0;
    int z = 0;
    char **tab;
    int words_count = count_words(str);
    int char_count = count_char(str);
    
    tab = malloc(sizeof(char *) * (count_words(str) + 1));
    while (str[x] != '\0') {
	tab[y] = malloc(sizeof(char) * (my_strlen(str) + 1));
	while (detect(str[x]) == 0) {
	    x++;
	}
	while (str[x] != '\0' && detect(str[x]) == 1) {
	    tab[y][z] = str[x];
	    z++;
	    x++;
	}
	tab[y][z] = '\0';
	y++;
	z = 0;
    }
    tab[y + 1] = NULL;
    return (tab);
}
int main()
{
    char **result;
    result = my_str_to_word_array("   exo de merde   ta race");
    my_show_word_array(result);
}
