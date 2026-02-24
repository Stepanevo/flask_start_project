# Flask quick-start (готовый проект)

## Что внутри
- `app.py` — Flask приложение
- `templates/hello.html` — шаблон (Jinja)
- `static/style.css` — стили
- `requirements.txt` — зависимости

## Запуск в VS Code (Windows)
1) Открой эту папку в VS Code: **File → Open Folder**
2) Открой терминал: **Terminal → New Terminal**
3) Создай виртуальное окружение:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   Если PowerShell ругается на политику, можно временно разрешить:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

4) Установи зависимости:
   ```powershell
   pip install -r requirements.txt
   ```

5) Запусти:
   Вариант A (самый простой):
   ```powershell
   python app.py
   ```
   Вариант B (через flask CLI):
   ```powershell
   flask --app app run --debug
   ```

6) Открой в браузере:
   - 

## Запуск (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Маршруты
- `/` — главная
- `/hello?name=Stepan`
- `/hello-page/Stepan`
- `/user/<username>`
- `/post/<int:post_id>`
- `/api/me` — JSON
