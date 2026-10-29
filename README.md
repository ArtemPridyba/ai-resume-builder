# AI Resume Builder
 
## Призначення системи
Вебзастосунок для автоматизованого створення та аналізу резюме з використанням штучного інтелекту.
Проєкт розробляється в межах дисципліни «Технології розроблення програмних систем».
 
## Функціональність
- реєстрація та автентифікація користувачів;
- створення й редагування резюме (WYSIWYG-конструктор);
- AI-генерація та покращення текстів резюме;
- ATS-аналіз резюме та порівняння з вакансією;
- експорт резюме у PDF/DOCX.
- підтримка української та англійської мов.
 
## Використані технології
| Рівень | Технології |
| --- | --- |
| Клієнт | React, TypeScript, Vite, Tailwind CSS, Zustand |
| Сервер | Python, FastAPI, Pydantic, Celery, Redis |
| Дані | PostgreSQL (pgvector), Cloudflare R2 / AWS S3 |
| Зовнішні сервіси | OpenAI API, Google Gemini API |
 
## Структура репозиторію
```ai-resume-builder/
├── README.md
├── .gitignore
├── docs/              # документація, ADR
│   └── adr/
├── backend/           # серверна частина (Python, FastAPI)
│   ├── app/
│   └── tests/
└── frontend/          # клієнтська частина (React, TypeScript)
    └── src/

```
 
## Запуск проєкту
серверна частина (віртуальне середовище .venv у корені проєкту):
```
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend
uvicorn app.main:app --reload
```

тести:
```
pip install pytest
cd backend
pytest
```

клієнтська частина:
```
cd frontend
npm install
npm run dev
```
