"""
Hands-On 1 Notes

1. Request–Response Cycle

Browser
   ↓
URL Router (urls.py)
   ↓
View (views.py)
   ↓
Model (Database Query)
   ↓
Response
   ↓
Browser


2. Middleware

Middleware sits between the incoming request and the outgoing response.

Examples:
• SecurityMiddleware – Adds security headers and HTTPS support.
• SessionMiddleware – Handles user sessions.


3. WSGI vs ASGI

WSGI
- Supports synchronous applications.
- Used by Django by default.

ASGI
- Supports asynchronous applications.
- Used for WebSockets, chat apps, and real-time features.


4. MVC vs Django MVT

MVC

Model      → Django Model
View       → Django Template
Controller → Django View
"""