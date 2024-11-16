all: rebuild

build:
	npm run build:css

rebuild:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	npm run build:css

clean:
	rm -f requirements.txt

fclean: clean

re: fclean all

.PHONY: all build rebuild clean fclean re
