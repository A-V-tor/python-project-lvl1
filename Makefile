install: #установка   зависимостей
	poetry install
brain-even: #запуск умных игр
	poetry run brain-even
brain-calc: #запуск умных игр
	poetry run brain-calc
build: #упаковка пакета
	poetry build
publish: #публикация проекта без добавления в индекс
	poetry publish --dry-run
package-install: #установка пакета
	python3 -m pip install --user dist/hexlet_code-0.3.0-py3-none-any.whl
lint: #запуск линтера
	poetry run flake8 brain_games
