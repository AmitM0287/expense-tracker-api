### 🧾 AMKR Studio API ###

AMKR Studio is a Django-based backend service providing utilities for budgeting, media downloading, and AI tools, built with modern authentication and deployment standards.

---

### 🚀 Features ###

- 🔊 Text-to-speech conversion
- 📥 YouTube video & Shorts downloader
- ✂️ Video splitter (into X parts)
- 🔐 2FA authentication support
- 🔑 Google OAuth login integration
- 👤 Traditional username-password login
- 🛠️ Modular Django APIs with JWT Auth

---

### 🐍 Python Version ###

- Python: `3.12.10`
- Pip: `25.0.1`
- PostgreSQL: `16`
- ffmpeg: `7.1.1`

---

### 📁 Naming Convention ###

| Type        | Convention |
|-------------|------------|
| File names  | `snake_case` |
| Variables   | `camelCase` |

---

### 🛠️ Development Setup ###

- Clone the repo:
```bash
git clone https://github.com/amitkrishnadev/amkr-studio-api.git && cd amkr-studio-api
```

- Create virtual environment:
```bash
python3 -m venv venv && source venv/bin/activate
```

- Install requirements:
```bash
pip install --no-cache-dir -r requirements.txt
```

- Run server:
```bash
python manage.py runserver
```

---

### 🐳 Docker Versions ###

- Python Base Image: `python:3.12-alpine`

---

### ✍️ Credits ###

- 🧑🏻‍💻 Amit Manna
- 🙏🏻 The Supreme Lord Kṛṣṇa

---

### 📚 References ###

- https://xlsxwriter.readthedocs.io/example_chart_combined.html
- https://xlsxwriter.readthedocs.io/chart_examples.html#chart-examples

---

### 📋 Tasks [In Progress] ###

- [x] JWT-based authentication
- [ ] Google OAuth integration
- [x] YouTube downloader (video & shorts)
- [x] Video splitter API
- [x] Text-to-speech (multi-language)
- [ ] Admin panel for user data management
- [ ] Group-based permissions
- [x] Media cleanup & storage rotation

---
