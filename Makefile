# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfrisby <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/11/26 18:30:39 by mfrisby           #+#    #+#              #
#    Updated: 2017/05/25 14:17:25 by mfrisby          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME_COL = Colleen
NAME_GRA = Grace
NAME_SUL = Sully

SRC_COL = 	Colleen.c
SRC_GRA = 	Grace.c
SRC_SUL = 	Sully.c

OBJ_COL = $(SRC_COL:.c=.o)
OBJ_GRA = $(SRC_GRA:.c=.o)
OBJ_SUL = $(SRC_SUL:.c=.o)

FLAG =	-Wall -Wextra -Werror

LIBFT = libft/libft.a

all: $(NAME_COL) $(NAME_GRA) $(NAME_SUL)

$(NAME_COL):
	@cc $(FLAG) $(SRC_COL) $(INCLUDE) -o $(NAME_COL)
	@echo "Colleen.c"
$(NAME_GRA):
	@cc $(FLAG) $(SRC_GRA) $(INCLUDE) -o $(NAME_GRA)
	@echo "Grace.c"
$(NAME_SUL):
	@cc $(FLAG) $(SRC_SUL) $(INCLUDE) -o $(NAME_SUL)
	@echo "Sully.c"

clean:
	@rm -rf obj
	@echo "\033[33mclean\033[m"

fclean: 		clean
	@/bin/rm -f $(NAME_COL) $(NAME_GRA) $(NAME_SUL)
	@echo "\033[33mfclean\033[m"

re: 			fclean all

.PHONY = 		all clean fclean re
