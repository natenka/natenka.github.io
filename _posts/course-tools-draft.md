## pytest


```
[pytest]
required_plugins = pytest-clarity>=0.3.0a0
addopts = -vv --no-hints --no-header
]
```


Проверка что тест вызван через pytest ..., а не python ...

```
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")
```
