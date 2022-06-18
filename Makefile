install: #установка   зависимостей
	poetry install
brain-games:
	poetry run brain-games
brain-even: #запуск умных игр
	poetry run brain-even
brain-calc: #запуск умных игр
	poetry run brain-calc
brain-gcd: #запуск умных игр
	poetry run brain-gcd
brain-progression: #запуск умных игр
	poetry run brain-progression
brain-prime: #запуск умных игр
	poetry run brain-prime

build: #упаковка пакета
	poetry build
publish: #публикация проекта без добавления в индекс
	poetry publish --dry-run
package-install: #установка пакета
	python3 -m pip install --user dist/hexlet_code-0.6.0-py3-none-any.whl
lint: #запуск линтера
	poetry run flake8 brain_games
inst: # обновление пакета
	python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.6.0-py3-none-any.whl
