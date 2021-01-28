---
title: "Мои текущие инструменты для онлайн курса"
date: 2021-02-02
tags:
 - toolset
category:
 - tools
---


* слайды: формат: markdown, показ: lookatme
* онлайн лекции: FCC
* запись лекций: OBS, FCC как бекап
* code: ipython, vim, tmux
* микрофон: blue yeti, плюс стойка; новая версия радио система
* скрипты для слушателей
* мои скрипты для проверки заданий
* общение на курсе: slack
* посты с информацией по курсу, инструкции: Github Pages


### ОС

Работаю на Windows. Технически всё время работаю на виртуалке с Debian, но хост Windows.
Поначалу хотела снести Windows и поставить Linux, но всё время было некогда, а потом втянулась и пока никаких неудобств нет.

### Текстовый редактор

Код, статьи, книги - всё пишу в vim.

__Так выглядит мой vim__
![alt]({{ site.url }}{{ site.baseurl }}/assets/images/vim.png)


Полезные ссылки:

* [Мой vimrc](https://github.com/natenka/dotfiles/blob/master/vimrc)
* [Лекция по основам vim](https://www.youtube.com/playlist?list=PLah0HUih_ZRkiQXDuElo_JW9OfmbEXRpj)

### Terminal/tmux

Как менеджер подключений использую [mRemoteNG](https://mremoteng.org/). В моем случае, это только SSH.
Так как я выбирала его достаточно давно, уже не вспомню чем меня не устроили другие варианты, но приглянулся именно он и пару лет пользуюсь без проблем.

На Windows по сути не работаю, поэтому могу только посоветовать использовать на Windows [cmder](https://cmder.net/) как терминал.
Очень сильно упрощает жизнь, особенно, если вы привыкли работать на Linux.

После своей же лекции по tmux, стала использовать его намного больше. До этого использовала только на курсе на лекциях. Спустя два месяца более активного использования, не представляю почему раньше не внедрила его в рабочий процесс.

![alt]({{ site.url }}{{ site.baseurl }}/assets/images/tmux.png)

Полезные ссылки:

* [Мой конфигурационный файл tmux](https://github.com/natenka/dotfiles/blob/master/tmux.conf)
* [Пример файла для создания сессии](https://github.com/natenka/dotfiles/blob/master/tmux_pyneng_session.conf)
* [Лекция по основам tmux](https://www.youtube.com/playlist?list=PLah0HUih_ZRkSAPJyzlk_wU7iVLzGFMAi)
* [Шпаргалка и ссылки по tmux](https://natenka.github.io/linux/tmux-basics/)

### Readthedocs

Книги перевела с Gitbook на Read the Docs. Главная причина - отстутствие PDF на новой версии GitBook (на тот момент).
Немного перестроилась и всем довольна.

* [Python для сетевых инженеров](https://pyneng.readthedocs.io/ru/latest/)
* [Ansible для сетевых инженеров](https://ansible-for-network-engineers.readthedocs.io)
* [Advanced Python для сетевых инженеров](https://pyneng2.readthedocs.io/en/latest/)


### Toggl

Toggl остается одним из моих любимых инструментов.
[Toggl](https://toggl.com/) позволяет отслеживать время потраченное на задачу.

> Toggl не включается сам и не отслеживает автоматически в каком софте вы сидите или на каком сайте.

__Toggl desktop__

![alt]({{ site.url }}{{ site.baseurl }}/assets/images/toggl_desktop.png)

Таймер нужно запускать вручную. И это однозначно не всем подходит. Как и в принципе идея отслеживать время. К этому надо привыкнуть. 
Мне наоборот нравится то, что надо вручную включать таймер, потому что это требует осознанности.
Конечно, бывают периоды, когда я выпадаю, и не использую его. Но процентов 90-95 времени в год, я всё же им пользуюсь.

Последние полтора года перестала отслеживать время на чтение/прослушивание книг. В основном потому что процесс наладился и без этого и я отмечаю прочитанное на [goodreads](https://www.goodreads.com/user/show/59424483-natasha-samoylenko).

В Toggl отличные отчеты, в которых можно делать срезы: неделя, месяц, год, произвольный период. Фильтровать по проекту, по названию задачи, по тегам.

__Отчет Toggl__
![alt]({{ site.url }}{{ site.baseurl }}/assets/images/toggl_report.png)

