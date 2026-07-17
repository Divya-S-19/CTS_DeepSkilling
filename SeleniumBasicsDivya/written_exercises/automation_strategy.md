# HANDS-ON 3
# Test Automation Process, Lifecycle & Framework Types

---

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether to Automate a Test Case

### 1. Repetitive Execution
Tests that are executed frequently should be automated because they save time and effort.

**Application to Scenario:**
The POST `/api/courses/` endpoint is tested after every code change, making it a good candidate for automation.

---

### 2. Stable Functionality
Automation is suitable for features that do not change frequently.

**Application to Scenario:**
The course creation API is a core feature with stable behavior, making automation effective.

---

### 3. High Business Impact
Critical features should be automated to detect defects quickly.

**Application to Scenario:**
Course creation is an essential function for the Course Management System, so it should be automated.

---

### 4. Regression Testing
Regression tests are repeated after every update, making them ideal for automation.

**Application to Scenario:**
The POST endpoint should be tested automatically whenever new changes are made.

---

### 5. Data-Driven Testing
Tests requiring multiple input combinations are suitable for automation.

**Application to Scenario:**
Different course names, codes, departments, and credits can be tested automatically using multiple datasets.

---

## 18. Automate or Manual Decision

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| Regression test for all CRUD endpoints | **Automate** | Executed after every code change and repetitive. |
| Exploratory testing of a new search feature | **Manual** | Requires human observation and creativity. |
| Performance test with 100 concurrent users | **Automate** | Load testing tools can simulate multiple users efficiently. |
| UI test for the login form | **Automate** | Frequently executed and suitable for Selenium automation. |
| Verify Swagger API documentation | **Manual** | Mostly involves reviewing documentation for correctness. |
| Smoke test after deployment | **Automate** | Quick verification that the application is running correctly. |

---

## 19. Test Automation ROI

### Definition

**Test Automation ROI (Return on Investment)** measures whether the time and effort spent developing automation are recovered through repeated execution.

### Calculation

Automation development time = **4 hours**

Manual execution time = **30 minutes (0.5 hours)**

Without maintenance:

4 ÷ 0.5 = **8 runs**

Automation pays for itself after approximately **8 executions**.

### Maintenance Overhead

After the 10th run, each execution requires:

20% × 30 minutes = **6 minutes (0.1 hour)**

Automation still provides significant time savings because maintenance time is much lower than manual execution time.

---

## 20. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application.

### Example

A Selenium test clicks a button before it becomes clickable, causing random failures depending on page loading speed.

### How to Prevent Flaky Tests

1. Use Explicit Waits instead of `time.sleep()`.
2. Use reliable locators such as ID or CSS selectors.
3. Ensure each test is independent and starts with a clean browser session.

---

# Task 2: Compare Automation Framework Types

## 21. Framework Types

### 1. Linear Framework

**Description:**
A simple framework where test scripts are written sequentially without reusable components.

**Advantage:**
Easy to learn and implement.

**Disadvantage:**
Poor maintainability and code duplication.

**Example:**
Automating a single Course Creation workflow.

---

### 2. Modular Framework

**Description:**
The application is divided into reusable modules, with each module having its own scripts.

**Advantage:**
Reusable code and easier maintenance.

**Disadvantage:**
Requires planning and modular design.

**Example:**
Separate modules for Login, Course, Student, and Enrollment.

---

### 3. Data-Driven Framework

**Description:**
Test data is stored separately (Excel, CSV, JSON) while the same test script runs with multiple datasets.

**Advantage:**
Supports testing many input combinations.

**Disadvantage:**
Requires external data management.

**Example:**
Testing course creation with multiple course names and codes.

---

### 4. Keyword-Driven Framework

**Description:**
Test actions are represented using keywords such as Login, Click, EnterText, and Submit.

**Advantage:**
Non-technical testers can create test cases.

**Disadvantage:**
Framework implementation is more complex.

**Example:**
Business analysts create test cases using predefined keywords.

---

### 5. Hybrid Framework

**Description:**
A combination of Modular, Data-Driven, and Keyword-Driven frameworks. It provides flexibility, reusability, and maintainability.

**Advantage:**
Highly scalable and widely used in real-world automation projects.

**Disadvantage:**
Initial setup is more complex.

**Example:**
Large Course Management projects with reusable page objects, external test data, and keyword support.

---

## 22. Recommended Framework

### Recommendation

A **Hybrid Framework** is the best choice.

### Justification

- Supports testing with **50 different user/password combinations** using a Data-Driven approach.
- Reuses login functionality across **20 test cases** using Modular design.
- Allows both technical and non-technical team members to create tests through Keyword-Driven features.
- Easier to maintain and extend as the project grows.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/

│
├── config/
│   └── config.py
│
├── test_data/
│   ├── login_data.xlsx
│   └── course_data.xlsx
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── base_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_course.py
│   └── test_student.py
│
├── utilities/
│   ├── browser.py
│   ├── logger.py
│   └── helpers.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

### Purpose of Each Folder

- **config/** – Stores project configuration.
- **test_data/** – Stores Excel, CSV, or JSON test data.
- **pages/** – Contains Page Object Model classes.
- **tests/** – Contains Selenium test scripts.
- **utilities/** – Common helper functions and browser setup.
- **reports/** – Stores execution reports.
- **screenshots/** – Stores screenshots captured during failures.

---

# Conclusion

Automation should focus on repetitive, stable, and high-priority test cases. A Hybrid Framework combines the strengths of Modular, Data-Driven, and Keyword-Driven approaches, making it the preferred choice for large Selenium automation projects.