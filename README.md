# 🚀 Real-Time Chat Application

A **scalable, real-time chat application** built using Django, WebSockets, and Redis.
This project demonstrates **event-driven architecture, real-time communication, and containerized deployment**.

---

## 📸 Demo

* Real-time messaging across multiple users
* Secure login & signup system
* Messages sync instantly across tabs/devices

---

## 🧠 Architecture Overview

```text
Client (Browser)
      ⇄ WebSocket (WSS)
Django Channels (ASGI - Daphne)
      ⇄ Redis (Pub/Sub Message Broker)
      ↓
Database (SQLite / PostgreSQL)
```

---

## ⚡ Features

* 🔴 **Real-Time Messaging** using WebSockets
* 🔐 **User Authentication** (Signup/Login/Logout)
* 📡 **Redis Pub-Sub Architecture** for scalability
* 🐳 **Dockerized Setup** (multi-container)
* ⚙️ **Django Channels (ASGI)** for async communication
* 💬 Persistent message storage in database

---

## 🛠️ Tech Stack

* **Backend:** Django, Django Channels
* **Realtime:** WebSockets
* **Message Broker:** Redis
* **Database:** SQLite (dev) / PostgreSQL (prod-ready)
* **Deployment:** Docker, Daphne
* **Frontend:** HTML, CSS, JavaScript (AJAX + WebSockets)

---

## 🔥 Key Concepts Implemented

* Event-driven architecture
* Pub-Sub messaging with Redis
* WebSocket lifecycle handling
* Secure session-based authentication
* Inter-container communication in Docker
* Static file handling in production

---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/django-realtime-chat.git
cd django-realtime-chat
```

---

### 2️⃣ Run with Docker

```bash
docker-compose up --build
```

---

### 3️⃣ Access the app

* App: http://127.0.0.1:8000/
* Admin: http://127.0.0.1:8000/admin/

---

### 4️⃣ Create users

```bash
docker exec -it djangochat-web-1 python manage.py createsuperuser
```

---

## 🔐 Authentication Flow

* Users sign up or log in
* Django creates a session
* Session is stored securely via cookies
* WebSocket connections validate authenticated users

---

## 📡 Real-Time Message Flow

1. User sends message
2. WebSocket consumer receives it
3. Message stored in database
4. Published to Redis channel
5. Redis broadcasts to all connected clients
6. Clients receive message instantly

---

## 🐳 Docker Architecture

```text
web (Django + Daphne)
    ⇄
redis (message broker)
```

* Containers communicate via service names
* Avoids localhost issues (`127.0.0.1` bug fixed)

---

## ⚠️ Challenges Solved

* ❌ WebSocket 404 errors → Fixed via ASGI routing
* ❌ Redis connection issues in Docker → Used service-based networking
* ❌ Static files not loading → Configured STATIC_ROOT + collectstatic
* ❌ Real-time sync issues → Implemented group broadcasting

---

## 🌍 Deployment (Production Ready)

* ASGI server: Daphne
* Redis for scaling
* Dockerized services
* Ready for deployment on cloud platforms like Render

---

## 📌 Future Improvements

* 👥 Online user presence tracking
* ⌨️ Typing indicators
* 🔐 JWT-based authentication
* 🗄️ PostgreSQL migration
* ☁️ CI/CD + cloud deployment

---

## 💼 Resume Highlight

> Built a scalable real-time chat application using Django Channels, WebSockets, and Redis with Docker-based deployment and secure authentication.

---

## 👨‍💻 Author

* GitHub: https://github.com/RakshithSridharV

---

## ⭐ If you like this project

Give it a ⭐ — it helps a lot!
