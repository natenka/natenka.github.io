Как я использую pytest для проверки заданий. Например про нюансы. Например == вместо in.


```

# Checking that tests are being called correctly
from _pytest.assertion.rewrite import AssertionRewritingHook
if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")

```
