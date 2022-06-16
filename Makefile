install: #установка poetry
	poetry install
brain-games: #запуск умных игр
	poetry run brain-games
build: #упаковка пакета
	poetry build
publish: #публикация проекта без добавления в индекс
	poetry publish --dry-run
package-install: #установка пакета
	python3 -m pip install --user dist/*.whl
lint: #запуск линтера
	poetry run flake8 brain_games
