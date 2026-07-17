# HANDS-ON 2
# SDLC vs TDLC – V-Model & Agile QA Integration

---

# Task 1: V-Model Mapping

## 9. V-Model Diagram

```
             Development (SDLC)                     Testing (TDLC)

          Requirements -----------------------> Acceptance Testing

          System Design ----------------------> System Testing

      Architecture Design --------------------> Integration Testing

          Module Design -----------------------> Unit Testing

                      \                         /
                       \                       /
                        \                     /
                           Coding
```

### SDLC Phases
1. Requirements
2. System Design
3. Architecture Design
4. Module Design
5. Coding

### TDLC Phases
1. Unit Testing
2. Integration Testing
3. System Testing
4. Acceptance Testing

---

## 10. SDLC ↔ TDLC Mapping with Test Artifacts

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan, Requirement Traceability Matrix (RTM) |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | All Testing Levels | Source Code & Executable Build |

---

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**
- Module coding completed.
- Unit test cases prepared.

**Exit Criteria**
- All unit tests executed.
- No critical defects remain.

---

### Integration Testing

**Entry Criteria**
- Unit testing completed.
- Modules integrated.

**Exit Criteria**
- Interfaces verified.
- Integration defects fixed.

---

### System Testing

**Entry Criteria**
- Integrated application available.
- Test environment ready.

**Exit Criteria**
- All system test cases passed.
- No Critical or High severity defects open.

---

### Acceptance Testing

**Entry Criteria**
- System testing completed successfully.
- Customer receives stable build.

**Exit Criteria**
- Customer approves the application.
- Application is ready for deployment.

---

## 12. Early QA Engagement

### 1. Requirements Review

QA reviews the Course Management API requirements to identify missing or unclear requirements before development begins.

Example:
Ensure the requirements specify whether duplicate course codes are allowed.

---

### 2. Design Review

QA reviews the API design and database schema to ensure they are testable.

Example:
Verify all API responses use proper HTTP status codes (200, 201, 400, 404, 500).

---

# Task 2: Agile QA and Shift-Left Testing

## 13. Problems in Waterfall Testing

### Problem 1

Defects are found very late, making them expensive and time-consuming to fix.

---

### Problem 2

Developers may need to rewrite completed modules if major bugs are discovered during testing.

---

### Problem 3

Project delivery may be delayed because testing starts only after development is completed.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.

---

### Daily Standup

- Report testing progress.
- Discuss blockers.
- Coordinate with developers.

---

### Sprint Review

- Verify completed features.
- Demonstrate tested functionality.
- Confirm acceptance criteria are met.

---

### Retrospective

- Discuss issues faced during testing.
- Suggest process improvements.
- Plan better testing practices for the next sprint.

---

## 15. Shift-Left Practices

### a) Requirement Review

QA reviews requirements before coding starts to identify ambiguities.

Example:
Ensure every API endpoint has clearly defined request and response formats.

---

### b) Writing Test Cases Before Code (TDD/BDD)

Prepare test cases before implementation.

Example:
Create test cases for POST `/api/courses/` before developers write the endpoint.

---

### c) Static Code Analysis

Analyze source code for coding standard violations and possible bugs before execution.

Example:
Use tools like SonarQube or Pylint to detect issues.

---

### d) API Contract Testing

Validate API request and response formats before integrating with frontend applications.

Example:
Verify POST `/api/courses/` accepts valid JSON and returns the expected status codes.

---

## 16. Acceptance Criteria (Given-When-Then)

### Scenario 1 – Happy Path

**Given**
The college admin is logged into the system.

**When**
The admin enters valid course details and submits the form.

**Then**
A new course is created successfully with HTTP 201 Created.

---

### Scenario 2 – Duplicate Course Code

**Given**
A course with code "CS101" already exists.

**When**
The admin submits another course using the same code.

**Then**
The system displays an error message indicating that the course code already exists.

---

### Scenario 3 – Missing Required Fields

**Given**
The admin opens the Create Course page.

**When**
The admin submits the form without entering mandatory fields.

**Then**
The system displays validation errors and the course is not created.

---

# Conclusion

The V-Model establishes a direct relationship between development and testing activities. Agile encourages continuous QA involvement throughout the project, while Shift-Left Testing helps detect defects early, reducing cost and improving software quality.