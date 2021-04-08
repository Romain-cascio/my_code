##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## 
##

NAME    	=       matchstick

SRC		=	matchstick.c\
			play.c\
			all_stars.c\
			algo_robot.c\
			my_printf.c\
			my_putnbr_base.c\
			my_put_nbr.c\
			my_strlen.c\
            my_putstr.c\
			my_get_nbrB.c\
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
