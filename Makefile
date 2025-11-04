.PHONY: install brain-games build package-install publish clean help

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install: build
	uv tool install dist/*.whl

publish: build
	@echo "Для публикации на PyPI:"
	@echo "uv publish"

clean:
	rm -rf dist/ build/ *.egg-info/

help:
	@echo "Доступные команды:"
	@echo "  make install          - Установить зависимости"
	@echo "  make brain-games      - Запустить игру"
	@echo "  make build            - Собрать пакет"
	@echo "  make package-install  - Установить пакет в систему"
	@echo "  make clean            - Очистить"
	@echo "  make help             - Справка"

lint:
	uv run ruff check brain_games

format:
	uv run ruff format brain_games

lint-fix:
	uv run ruff check --fix brain_games
