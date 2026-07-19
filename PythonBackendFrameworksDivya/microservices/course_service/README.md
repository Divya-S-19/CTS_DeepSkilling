# Hands-On 10 – Microservices Architecture

## Service Decomposition

| Service | Responsibility | Endpoints | Database |
|----------|---------------|-----------|----------|
| Course Service | Manage courses | /api/courses | courses.db |
| Student Service | Manage students and enrollments | /api/students | student.db |
| Auth Service | User authentication | /login, /register | auth.db |
| Notification Service | Email notifications | /notify | notification.db |

## Synchronous vs Asynchronous Communication

### Synchronous (HTTP)
- Immediate response
- Easy to implement
- Tight coupling
- Service failure affects dependent services

### Asynchronous (RabbitMQ/Kafka)
- Loose coupling
- Better scalability
- Eventual consistency
- Suitable for notifications, emails, logging, analytics