# README

pydantic v2가 v1보다 빠른건 내부 validation 로직이 rust로 구현되어 있기 때문이라고 생각합니다.

[pydantic-core](https://github.com/pydantic/pydantic-core?tab=readme-ov-file#pydantic-core)

## 퍼포먼스 비교

### v1

```bash
poetry run python main.py

Elapsed time: 3753.17ms
```

### v2

```bash
poetry run python main.py

Elapsed time: 953.12ms
```
