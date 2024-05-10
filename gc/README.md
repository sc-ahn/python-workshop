# GC의 오버헤드를 체감하기 위한 예제 코드입니다

```bash
Usage:
  make <target>

Targets:
  help                  지금 보고계신 도움말
  show-gc-threshold     gc 의 기본 threshold 값을 확인합니다.
  step1                 Dummy 객체를 다수 생성하고, 평균 및 최대 생성시간을 출력하는 예시입니다.
  step2                 gc 를 비활성화합니다.
  step3                 gc 가 활성화되어있지만, 사용안하는 객체를 제거하면 빨라집니다.
  step4                 gc 가 활성화되어있지만, 라이브러리가 생성한 객체들에 대해 scan하지 않도록 합니다.
  step5                 gc 가 활성화되어있지만, gen2 GC 발생빈도를 낮춰봅니다.
```
