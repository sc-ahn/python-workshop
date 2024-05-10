MAKEFLAGS += --silent

help: ## 지금 보고계신 도움말
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-0-9]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

show-gc-threshold: ## gc 의 기본 threshold 값을 확인합니다.
	echo 'gc 의 기본 threshold 값을 확인합니다.'
	echo ''
	poetry run python gc_default_setting.py

step1: ## Dummy 객체를 다수 생성하고, 평균 및 최대 생성시간을 출력하는 예시입니다.
	echo 'Dummy 객체를 다수 생성하고, 평균 및 최대 생성시간을 출력하는 예시입니다.'
	echo '메모리에 존재하는 객체를 더 많이 늘려주기 위해'
	echo '사용하지 않지만 pytorch, numpy 등의 라이브러리를 import 했습니다.'
	echo ''
	poetry run python gc_enabled_1.py

step2: ## gc 를 비활성화합니다.
	echo 'gc 를 비활성화합니다.'
	echo ''
	poetry run python gc_disabled_1.py

step3: ## gc 가 활성화되어있지만, 사용안하는 객체를 제거하면 빨라집니다.
	echo 'gc 가 활성화되어있지만, 사용안하는 객체를 제거하면 빨라집니다.'
	echo ''
	poetry run python gc_enabled_2.py

step4: ## gc 가 활성화되어있지만, 라이브러리가 생성한 객체들에 대해 scan하지 않도록 합니다.
	echo 'gc 가 활성화되어있지만, 라이브러리가 생성한 객체들에 대해 scan하지 않도록 합니다.'
	echo ''
	poetry run python gc_modified_1.py

step5: ## gc 가 활성화되어있지만, gen2 GC 발생빈도를 낮춰봅니다.
	echo 'gc 가 활성화되어있지만, gen2 GC 발생빈도를 낮춰봅니다.'
	echo ''
	poetry run python gc_modified_2.py
