MAKEFLAGS += --silent
path := .

.PHONY: help
help: ## what you are looking at
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: test
test: ## run tests
	@echo "Running tests locally"
	@poetry run pytest --log-cli-level=INFO

.PHONY: report
report: ## generate report
	@echo "Starting report server"
	@echo "Open http://localhost:12800 in your browser"
	@poetry run python -m http.server --directory . 12800
