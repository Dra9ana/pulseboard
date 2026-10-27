.PHONY: flct

flct:
	uv run ruff format --check apps
	uv run ruff check apps
	uv run pytest
