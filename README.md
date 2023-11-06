<div class="Markdown base-markdown base-markdown_with-gallery markdown markdown_size_normal markdown_type_theory full-markdown"><h1 align="center">Финальный проект спринта: приложение QRKot</h1><div class="paragraph">Приложение для Благотворительного фонда поддержки котиков <strong>QRKot</strong>. </div><div class="paragraph">Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.</div><div class="paragraph"><img src="https://pictures.s3.yandex.net:443/resources/sprint2_picture1_1672399951.png" alt="" crossorigin="anonymous" class="image image_expandable"></div></div><div class="paragraph"><h3>Проекты</h3></div><div class="paragraph">В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.</div><div class="paragraph">Пожертвования в проекты поступают по принципу <em>First In, First Out</em>: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.</div><div class="paragraph"><h3>Пожертвования</h3></div><div class="paragraph">Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.</div><div class="paragraph"><h3>Пользователи</h3></div><div class="paragraph">Целевые проекты создаются администраторами сайта. </div><div class="paragraph">Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.</div><div class="paragraph">Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.</div>
<h3>Документация</h3>

Документация API в формате `swagger` будет доступна после запуска по адресу:

```
http://localhost:8000/docs
```

В формате `redoc`:

```
http://localhost:8000/redoc
```

<h2 align="center"> Локальный запуск проекта </h2>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:tarrim80/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Применить миграции:

```
alembic upgrade head
```
Запустить приложение на локальном сервере:

```
uvicorn app.main:app
```

<div align="center">

### Используемые технологии:

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python&logoColor=FFFFFF)](https://www.python.org/)&nbsp;&nbsp;![github](https://img.shields.io/badge/github-464646?style=flat-square&logo=github&logoColor=FFFFFF)&nbsp;&nbsp;![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=FastAPI&logoColor=white&link=https%3A%2F%2Ffastapi.tiangolo.com%2F)&nbsp;&nbsp;![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite&logoColor=white)&nbsp;&nbsp;![SQLAlchemy](https://github.com/tarrim80/badges-and-icons/raw/main/technologies_badges/sql_alchemy.svg)&nbsp;&nbsp;![Insomnia](https://img.shields.io/badge/-Insomnia-464646?style=flat-square&logo=Insomnia&logoColor=white&link=https%3A%2F%2Finsomnia.rest%2F)&nbsp;&nbsp;![Postman](https://img.shields.io/badge/-Postman-464646?style=flat-square&logo=Postman&logoColor=white)&nbsp;&nbsp;![Swagger](https://img.shields.io/badge/-Swagger-464646?style=flat-square&logo=Swagger&logoColor=white&link=https%3A%2F%2Fswagger.io%2F)
</div>
<div align="center">

### Выполнено в рамках прохождения курса "Python-разработчик плюс" на ["Яндекс&nbsp;Практикум"](https://practicum.yandex.ru/)
</div>
