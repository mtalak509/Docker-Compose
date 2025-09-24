# Docker-Compose
**Инструкция**
1. Скачайте файлы репозитория в отдельную лопальную папку
2. в папке с ботом откройте dockerfile и укажите токен бота:
   ```dockerfile
    ENV TOKEN='YOUR_BOT_TOKEN_HERE'
    ```
3. Откройте SSH терминал в корне папки, где находится docker-compose.yaml
4. Соберите образы с помощью команды:
   ```bash
    docker compose up --build
    ```
5. Проверьте статус работы контейнеров:
   ```bash
    docker ps
    ```
6. Для остановки docker compose используйте:
   ```bash
    docker compose down
    ```
7. Для повторного запуска используйте:
    ```bash
    docker compose up
    ```
