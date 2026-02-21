# TestTask Telegram Bot 🤖✨

README сгенерирован AI - считаю, такие задачи можно делегировать.

## Обзор 📌
Проект — Telegram‑бот на `aiogram 3`, который принимает сообщения пользователя, отправляет их в OpenAI Responses API и сохраняет историю диалога в PostgreSQL. Поддерживаются команды `/start`, `/help` и кнопка «Новый запрос» для очистки истории.

## Стек 🧰
- Python 3.12
- aiogram 3
- OpenAI Python SDK (Responses API)
- PostgreSQL 16 + SQLAlchemy (async) + Alembic
- Docker + docker‑compose
- uv

## Функционал 🚀
- Ответы ИИ на сообщения пользователя 💬
- Хранение последних 30 сообщений в БД для контекста 🗂️
- Команды бота и очистка истории диалога 🧹
- Автоматический запуск миграций при старте контейнера ⚙️

## Переменные окружения 🧪
Файл окружения расположен в `src/.env`.

Пример:

```env
ENV=dev/prod

OPENAI_TOKEN=sk-your-openai-token
BOT_TOKEN=123456789:your-telegram-bot-token

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=zaBotaTestTask
POSTGRES_HOST=postgres
```


## Быстрый старт (Docker) 🐳
1. Заполните `src/.env`.
2. Запустите контейнеры:

```bash
docker compose up --build
```

Бот запустится, а миграции применятся автоматически через `entrypoint.sh`.

## Команды бота 🧭
- `/start` — очистить историю диалога и начать заново 🔄
- `/help` — справка 🆘
- Кнопка «Новый запрос» — очистка истории 🧽

## Структура проекта 🗺️
- `src/app.py` — точка входа
- `src/handlers/` — обработчики сообщений и команд
- `src/services/` — бизнес‑логика (AI и сообщения)
- `src/database/` — модели, репозитории, миграции
- `src/data/config.py` — настройки и env
- `docker-compose.yaml` и `Dockerfile` — контейнеризация
