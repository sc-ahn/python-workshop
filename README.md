# python-workshop

Python을 사용하면서 기록하고 싶었던 내용을 dockerizing 하여 기록하는 저장소입니다.

> 각각의 실행환경이 다를 것이고, 이를 매번 맞춰주는 것은 번거롭기에 도커화하여 기록합니다.

| 목차 | 내용 |
| --- | --- |
| [concurrent](./concurrent) | 병렬프로그래밍 퍼포먼스를 비교하기위해 작성 |
| [gc](./gc) | GC 오버헤드 설명 및 튜닝관련 내용 |
| [list vs. array](./list_vs_array) | built-in list와 array 그리고 numpy의 ndarray 성능 비교 |
| [pydantic v1 vs. v2] | pydantic v1과 v2의 성능 비교 |

## 실행

Makefile에 커맨드를 작성해두었습니다.

```bash
> make help

Usage:
  make <target>

Targets:
  help                  make help
  build-gc              -> make run-gc or make shell-gc
  build-cc              -> make shell-cc
  build-cc-py312        -> make shell-cc-py312
  build-list-vs-array   -> make shell-list-vs-array
  build-use-pydantic-v1  -> make shell-use-pydantic-v1
  build-use-pydantic-v2  -> make shell-use-pydantic-v2
```
