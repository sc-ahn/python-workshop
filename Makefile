help: ## make help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

build-gc: ## -> make run-gc or make shell-gc
	docker build -t python-workshop-gc -f gc.Dockerfile .

run-gc:
	docker run -it --rm \
		-v ./gc:/d3fau1t/workshop/gc \
		-v ./pyproject.toml:/d3fau1t/workshop/pyproject.toml \
		-v ./poetry.lock:/d3fau1t/workshop/poetry.lock \
		python-workshop-gc

shell-gc:
	docker run -it --rm \
		-v ./gc:/d3fau1t/workshop/gc \
		python-workshop-gc \
		/bin/bash


build-cc: ## -> make shell-cc
	docker build -t python-workshop-concurrent -f concurrent.Dockerfile .

shell-cc:
	docker run -it --rm \
		-v ./concurrent:/d3fau1t/workshop \
		python-workshop-concurrent \
		/bin/bash


build-cc-py312: ## -> make shell-cc-py312
	docker build -t python-workshop-concurrent-py312 -f concurrent-py312.Dockerfile .

shell-cc-py312:
	docker run -it --rm \
		-v ./concurrent:/d3fau1t/workshop \
		python-workshop-concurrent-py312 \
		/bin/bash

build-list-vs-array: ## -> make shell-list-vs-array
	docker build -t python-workshop-list-vs-array -f list-vs-array.Dockerfile .

shell-list-vs-array:
	docker run -it --rm \
		-v ./list_vs_array:/d3fau1t/workshop/list_vs_array \
		python-workshop-list-vs-array \
		/bin/bash

build-use-pydantic-v1: ## -> make shell-use-pydantic-v1
	docker build -t python-workshop-use-pydantic-v1 -f use-pydantic-v1.Dockerfile .

shell-use-pydantic-v1:
	docker run -it --rm \
		python-workshop-use-pydantic-v1 \
		/bin/bash

build-use-pydantic-v2: ## -> make shell-use-pydantic-v2
	docker build -t python-workshop-use-pydantic-v2 -f use-pydantic-v2.Dockerfile .

shell-use-pydantic-v2:
	docker run -it --rm \
		python-workshop-use-pydantic-v2 \
		/bin/bash

build-json-vs-orjson: ## -> make shell-json-vs-orjson
	docker build -t python-workshop-json-vs-orjson -f json-vs-orjson.Dockerfile .

shell-json-vs-orjson:
	docker run -it --rm \
		-v ./json-vs-orjson:/d3fau1t/workshop \
		-p 12800:12800 \
		python-workshop-json-vs-orjson \
		/bin/bash
