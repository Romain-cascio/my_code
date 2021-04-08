##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## 
##

SRC	=	my_printf.c \
		my_putchar.c \
		my_strlen.c \
		my_putnbr_base.c \
		my_putstr.c \
		my_getnbr.c \
		my_put_nbr.c

OBJ	=	$(SRC:.c=.o)

NAME    =       libmy.a

all:	$(NAME)

$(NAME):	$(OBJ)
	ar rc $(NAME) $(OBJ)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re:	fclean all

.PHONY: all clean fclean re
