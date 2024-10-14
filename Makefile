# Project commands
.PHONY: runserver
runserver:
	poetry run uvicorn src.main:app --host localhost --reload

.PHONY: migrate
migrate:
	poetry run alembic upgrade head

.PHONY: downgrade
downgrade:
	poetry run alembic downgrade -1 
