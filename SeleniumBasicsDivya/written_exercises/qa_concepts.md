# HANDS-ON 1
## QA Concepts, Functional Testing & Defect Lifecycle

---

# Task 1: Map Testing Types to a Real System

## 1. Test Levels

### Unit Testing
**Description:** Tests a single function independently.

**Test Case:**
Verify that the `create_course()` function correctly creates a course object when valid input is provided.

**Testing Type:** Functional Testing

---

### Integration Testing

**Description:** Tests the interaction between API endpoints and the database.

**Test Case:**
Send a POST request to `/api/courses/` and verify that the course is successfully stored in the database.

**Testing Type:** Functional Testing

---

### System Testing

**Description:** Tests the complete system from end to end.

**Test Case:**
Create a new course using the API and retrieve it using the GET endpoint to verify successful creation.

**Testing Type:** Functional Testing

---

### User Acceptance Testing (UAT)

**Description:** Tests from the end user's perspective.

**Test Case:**
A college administrator logs into the application, creates a new course, and confirms that the course appears in the course list.

**Testing Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Checks whether the application performs the required functionality correctly.

Examples:
- Create Course
- Update Course
- Delete Course
- Retrieve Course

### Non-Functional Testing

Checks how well the system performs.

Example:

**Performance Testing**

Verify that the GET `/api/courses/` endpoint responds within **2 seconds** when accessed by **100 concurrent users**.

---

## 3. Black-Box Testing vs White-Box Testing

### Black-Box Testing

- Internal code is unknown.
- Tester checks only inputs and outputs.
- Focuses on system functionality.

**Performed by:** QA Tester

---

### White-Box Testing

- Internal source code is known.
- Tests logic, conditions, loops, and code paths.

**Performed by:** Developer

---

## 4. Formal Test Cases

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API server running | Send POST request with valid course details | HTTP 201 Created and course stored successfully | | |
| TC002 | Create course with missing course name | API server running | Send POST request without course name | HTTP 400 Bad Request with validation error | | |
| TC003 | Create duplicate course | Existing course already available | Send POST request using existing course code | Duplicate course should not be created and appropriate error displayed | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Rejected

If the developer finds that the reported issue is not a valid defect, it is marked as **Rejected**.

### Deferred

If the defect is valid but fixing it is postponed to a future release, it is marked as **Deferred**.

---

## 6. Severity and Priority Classification

### a) POST /api/courses/ returns 500 Internal Server Error

Severity: **Critical**

Priority: **P1**

Reason:
The API cannot create any course, preventing users from performing a core function.

---

### b) Course names longer than 150 characters are silently truncated

Severity: **Medium**

Priority: **P2**

Reason:
Data is modified unexpectedly, but the application continues to function.

---

### c) Swagger documentation contains a typo

Severity: **Low**

Priority: **P4**

Reason:
Only documentation is affected; system functionality is not impacted.

---

### d) Login occasionally returns 401 for valid credentials

Severity: **High**

Priority: **P1**

Reason:
Users may fail to log in randomly, affecting reliability and user experience.

---

## 7. Defect Report

**Defect ID:** BUG-001

**Title:**
POST `/api/courses/` returns 500 Internal Server Error

**Environment:**
Windows 11, Python 3.10, FastAPI, Chrome Browser

**Build Version:**
Version 1.0

**Severity:**
Critical

**Priority:**
P1

**Steps to Reproduce:**

1. Start the Course Management API.
2. Open Swagger UI.
3. Select POST `/api/courses/`.
4. Enter valid course details.
5. Click Execute.

**Expected Result:**

Course should be created successfully and return HTTP 201.

**Actual Result:**

HTTP 500 Internal Server Error is returned.

**Attachments:**

Screenshot of 500 error.

---

## 8. Severity vs Priority

### Severity

Severity indicates how much the defect impacts the application.

### Priority

Priority indicates how quickly the defect should be fixed.

### Example

Suppose the company CEO's dashboard displays the company logo incorrectly.

- Severity: Low (only cosmetic)
- Priority: High (must be fixed immediately before a client presentation)

This shows that a bug can have **Low Severity** but **High Priority**.