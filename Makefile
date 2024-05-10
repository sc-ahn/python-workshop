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


build-cc:
	docker build -t python-workshop-concurrent -f concurrent.Dockerfile .

shell-cc:
	docker run -it --rm \
		-v ./concurrent:/d3fau1t/workshop \
		python-workshop-concurrent \
		/bin/bash


build-cc-py312:
	docker build -t python-workshop-concurrent-py312 -f concurrent-py312.Dockerfile .

shell-cc-py312:
	docker run -it --rm \
		-v ./concurrent:/d3fau1t/workshop \
		python-workshop-concurrent-py312 \
		/bin/bash
