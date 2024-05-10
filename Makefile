build-gc:
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
