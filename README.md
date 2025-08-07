<!-- PROJECT TITLE -->

# 📚 Library Management System

Modern full-stack web application for managing university-scale library operations – from book catalogs to student check-ins – built with a Django REST API and a Reactfront-end.

## Table of Contents

- [📚 Library Management System](#-library-management-system)
  - [Table of Contents](#table-of-contents)
  - [✨ Features](#-features)
  - [🏗️ Built With](#️-built-with)
  - [📂 Project Structure](#-project-structure)
  - [🚀 Getting Started](#-getting-started)
    - [Backend – Django API](#backend--django-api)
    - [Frontend – React Client](#frontend--react-client)
  - [🧩 Usage](#-usage)
  - [🗺️ Roadmap](#️-roadmap)
  - [🗂️ Acknowledgments](#️-acknowledgments)

---

## ✨ Features

• CRUD management for books, users and borrowing cards  
• Advanced search & filtering with multiple fields  
• Real-time statistics dashboards with interactive charts  
• Student check-in / check-out tracking  
• Responsive admin and student portals  
• Token-based authentication & role-based authorization  
• Binary image storage for book covers & avatars  
• Docker-ready production configuration (future roadmap)

---

## 🏗️ Built With

| Layer     | Tech Stack                                            |
| --------- | ----------------------------------------------------- |
| Front-end | React • React Router • Axios • TailwindCSS • Recharts |
| Back-end  | Python • Django • Django REST Framework               |
| Database  | PostgreSQL                                            |
| Tooling   | Git • Prettier • ESLint                               |

---

## 📂 Project Structure

```
Library-Management/
 ├─ Backend/               # Django project & apps
 │   ├─ models.py          # Auto-generated ORM models (reverse engineered)
 │   ├─ views.py           # REST viewsets / controllers
 │   └─ ...
 ├─ Frontend/              # React client
 │   ├─ App.js
 │   └─ Components/
 └─ README.md
```

---

## 🚀 Getting Started

Follow these instructions to get a **local development** copy up and running.

### Backend – Django API

```bash
# 1. Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt  # create this file or install manually

# 3. Apply migrations & create superuser
python manage.py migrate
python manage.py createsuperuser

# 4. Run development server
python manage.py runserver 8000
```

### Frontend – React Client

```bash
cd Frontend
npm install            # or pnpm install
npm run dev            # Vite dev server on http://localhost:5173
```

The client is configured to proxy API requests to `http://localhost:8000` during development (see `vite.config.js`). Adjust as needed.

---

## 🧩 Usage

1. Sign in as admin using the account you created earlier.
2. Navigate to **Books → Add** to import new titles.
3. Issue borrowing cards in **Students → Borrow**.
4. Monitor real-time charts in **Dashboard**.

Screenshots & GIF demonstrations live in the `images/` directory.

---

## 🗺️ Roadmap

- [x] User Management
- [x] Book Management
- [ ] Docker Compose for one-command setup
- [ ] CI/CD GitHub Actions workflow
- [ ] Unit & integration test suite (Pytest + React Testing Library)

See the **open issues** for full list of proposed features (and known issues).

---

## 🗂️ Acknowledgments

Made with ❤️ by the Library-Management team.
