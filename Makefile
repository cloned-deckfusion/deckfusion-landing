NAME = backend

all: $(NAME)

$(NAME):
	poetry export --without-hashes --format=requirements.txt > requirements.txt

clean:
	rm -f requirements.txt

fclean: clean

re: fclean all

.PHONY: all clean fclean re
