##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## 
##

NAME    	=       bsq

SRC		=		bsq.c\
				open_and_read_map.c\
				play.c\
				my_putchar.c\

OBJ		=	$(SRC:.c=.o)

all:	$(NAME)

$(NAME):	$(OBJ)
	gcc -o $(NAME) $(OBJ)
	rm -f $(OBJ)

clean:
	rm -f $(OBJ)

re:	fclean all

fclean: clean
	rm -f $(NAME)

.PHONY: all clean fclean re
