---
title: "Что нового в Python 3.9"
date: 2021-05-17
tags:
 - pyneng
category:
 - pyneng
---

Уже скоро выходит Python 3.10, а я только собралась рассказать про 3.9.
Тем не менее, надеюсь, кому-то пригодится.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLah0HUih_ZRn2hltZ0B3OoLfYdxjpDcES" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* [Запись лекции](https://youtube.com/playlist?list=PLah0HUih_ZRn2hltZ0B3OoLfYdxjpDcES)
* [Примеры кода](https://github.com/pyneng/pyneng-bonus-lectures/tree/master/examples/08_python39)
* [Слайды](https://github.com/pyneng/all-pyneng-slides/blob/main/bonus/python_3_9.md)
* [What's new in Python 3.9](https://docs.python.org/3/whatsnew/3.9.html)
* [Статья на RealPython](https://realpython.com/python39-new-features/)

Коротко о новых фичах:

* новые модули graphlib, zoneinfo
* новые методы строк removeprefix, removesuffix
* новые операции со словарями `|` и `|=`
* в аннотации типов вместо List/Dict/Tuple можно писать list/dict/tuple
* новый тип typing.Annotated
* в декораторах можно писать плюс-минус любое выражение, которое возвращает правильный вызываемый объект
* в asyncio новые корутины: asyncio.to_thread (вместо loop.run_in_executor), loop.shutdown_default_executor
