---
title: "Мои инструменты для онлайн курса. Часть 1"
date: 2020-05-25
tags:
 - toolset
category:
 - tools
---

Что я использую для курса:

* Лекции [FreeConferenceCall](https://www.freeconferencecall.com/downloads)
* Запись [OBS](https://obsproject.com/ru), FCC как бекап
* На youtube заливаю mkv, на google drive mp4, конвертация HandBrake. Avidemux для редактирования
* Чат [slack](https://slack.com/)
* вопросы во время лекции в slack
* Таймер [toggle mini timer](http://toggl.com/)
* Все выполняю на vm с debian. Часть примеров в ipython, остальное vim + tmux
* подготовленные виртуалки
* инструкции дублирующие информацию из лекции
* Лекции выкладываю на google drive и youtube
* Микрофон Blue Yeti
* Сайт курса - Github Pages
* Задания сдача/проверка git + github
* Проверка заданий pytest + скрипты, затем вручую
* Книга/методичка
* Правила: можно делать задания сколько угодно, бесплатно можно переходить на следующий курс, можно второй раз пройти курс бесплатно

### ОС

Работаю на Windows. Технически все время работаю на виртуалке с Debian, но хост Windows.
Поначалу хотела снести Windows и поставить Linux, но все время было некогда, а потом втянулась и пока никаких неудобств нет.

### Организация рабочего стола

Для меня очень важны такие вещи как высота стола, расположение клавиатуры и монитора.
Поэтому тут всё подстроено под меня по максимуму.
Работаю стоя, как правило, только во время лекций.

> Часто спрашивают зачем читаю курсы стоя: Лучше голос, сидя всё более лениво рассказывается. Как минимум, у меня точно так.

![alt]({{ site.url }}{{ site.baseurl }}/assets/images/desk.png)

### Текстовый редактор

Код, статьи, книги - все пишу в vim.

Не могу назвать себя продвинутым пользователем vim, но при переключении на другой редактор ощутимо не хватает того, что может vim. Хотя, конечно дело ещё и просто в привычке.


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

После своей же лекции по tmux стала намного больше использовать его. Спустя два месяца более активного использования, не представляю почему раньше не дошли руки нормально с ним разобраться.

![alt]({{ site.url }}{{ site.baseurl }}/assets/images/tmux.png)

Полезные ссылки:

* [Мой конфигурационный файл tmux](https://github.com/natenka/dotfiles/blob/master/tmux.conf)
* [Пример файла для создания сессии](https://github.com/natenka/dotfiles/blob/master/tmux_pyneng_session.conf)
* [Лекция по основам tmux](https://www.youtube.com/playlist?list=PLah0HUih_ZRkSAPJyzlk_wU7iVLzGFMAi)
* [Шпаргалка и ссылки по tmux](https://natenka.github.io/linux/tmux-basics/)

