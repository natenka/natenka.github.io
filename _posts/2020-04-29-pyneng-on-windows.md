---
title: "Выполнение заданий книги/курса на Windows"
date: 2020-04-29
tags:
 - pyneng
 - windows
category:
 - pyneng
---

Я протестировала все задания и тесты на Windows 10 и написала какие есть нюансы.

> Проверка выполнялась на "чистой" Windows. С WSL нюансы, которые описаны ниже, должны пропасть.

Напомню, что также есть [подготовленные виртуалки на Debian](https://pyneng.github.io/docs/course-vm/),
которые могут упростить работу, но иногда работать с виртуалкой не позволяют ресурсы или на хосте и так установлен Linux
или возникли проблемы с установкой виртуалки. В этом случае можно работать на хосте с Linux или Windows.
В книге и курсе все примеры на Linux, поэтому никаких уточнений нет, а вот на Windows есть некоторые нюансы и они перечислены ниже.

> Все проверки проводились на последних версиях всех сторонних модулей.

## Установка Python 3.7

Скачать и установить [Python 3.7](https://www.python.org/downloads/release/python-377/).
Обязательно поставить галочку "Add Python 3.7 to PATH".

После установки проверить:
```
python --version
```

Вывод должен быть: `Python 3.7.7`

> Если вы не будете использовать редактор Mu, можно установить и 3.8, но прежде
> лучше посмостреть на Mu. Для базовых тем, которые рассматриваются в курсе,
> изменений в 3.8 практически нет, поэтому можно спокойно использовать Python 3.7.

## Альтернативный вариант командной строки

Так как на курсе мы работаем с git, очень рекомендуется поставить [Cmder](https://cmder.net/).
Для этого надо выбрать "Download Full".

После установки Cmder в нем сразу доступен git и 
[надо разобраться как он работает и настроить его для работы с Github](https://pyneng.readthedocs.io/ru/latest/book/02_git_github/index.html).

> При желании, можно выполнить [дополнительные настройки](https://medium.com/@alif50/how-to-install-cmder-and-make-it-amazing-c8765e591de5)

## Установка Mu

Единственный нюанс с установкой Mu на windows - это то, что его лучше установить через pip,
чтобы модули, которые установлены в pip были видны. То есть, установить надо так:
```
pip install mu-editor
```

А не через установщик Windows.

[Остальные настройки аналогичны на Windows и Linux](https://pyneng.github.io/docs/mu/)

## Нюансы выполнения заданий

Модуль pexpect не работает на Windows и так как он не нужен для выполнения заданий,
это влияет только на то, что не получится повторить примеры из лекции.

Все остальные модули работают, но с некоторыми есть нюансы.

### graphviz

Для выполнения заданий в 11 и 17 разделе будет нужен graphviz.

Нужно установить модуль Python:
```
pip install graphviz
```

И приложение [graphviz](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)

После установки надо добавить [graphviz в PATH](https://bobswift.atlassian.net/wiki/spaces/GVIZ/pages/131924165/Graphviz+installation)

### csv

При работе с csv на Windows всегда надо указывать `newline=""` при открытии файла:
```
    with open(output, "w", newline="") as dest:
        writer = csv.writer(dest)
```

### textfsm

Часть модулей, которые использует textfsm, не доступны для Windows.
И в то же время, они не нужны для нашего использования textfsm. 
Чтобы textfsm коректно работал на Windows надо закоментировать
в файле terminal.py в каталоге textfsm некоторые строки.

Как найти каталог textfsm:

Сначала смотрим где находится каталог site-packages (вывод сокращен):
```
In [2]: import sys

In [3]: sys.path
Out[3]:
 '...appdata\\local\\programs\\python\\python37\\lib\\site-packages',
```

Затем переходим в этот каталог и внутри него ищем каталог textfsm.
В каталоге textfsm открываем файл terminal.py и комментируем строки таким образом:
```
# import fcntl
import getopt
import os
import re
import struct
import sys
# import termios
import time
# import tty
```

После этого код с использованием textfsm должен работать на Windows.

