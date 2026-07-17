 -- Task 1: Baseline Performance Hands-On 4
 USE college_db;
 EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- EXPLAIN Analysis
-- students table uses FULL TABLE SCAN (access_type = ALL)
-- because there is no index on enrollment_year.

-- EXPLAIN Analysis
-- students table uses FULL TABLE SCAN (access_type = ALL)
-- because there is no index on enrollment_year.
-- Estimated Query Cost = 4.35
-- Students rows examined = 8
-- Enrollments rows examined = 1
-- Courses rows examined = 1
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);
SHOW INDEX FROM students;

CREATE UNIQUE INDEX idx_enrollment_unique
ON enrollments(student_id, course_id);
CREATE INDEX idx_course_code
ON courses(course_code);
EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;
-- Comparison of Query Plans

-- Before Index:
-- students access_type = ALL
-- rows examined = 8

-- After Index:
-- students access_type = REF
-- index used = idx_students_enrollment_year
-- rows examined = 5

-- enrollments now uses:
-- idx_enrollment_unique
-- using_index = true

-- courses still uses ALL scan because
-- table size is very small (5 rows)
-- MySQL does not support PostgreSQL-style partial indexes.

-- Equivalent optimization:
CREATE INDEX idx_grade_student
ON enrollments(grade, student_id);

# N+1 Problem

# Query 1:
# SELECT * FROM enrollments

# Then for each enrollment:
# SELECT first_name,last_name
# FROM students
# WHERE student_id=?

# Total Queries:
# 1 + N

# Current Database:
# N = 10 enrollments
# Total = 11 queries

# JOIN Solution:
# 1 query only

# If 10,000 enrollments:
# N+1 Version = 10,001 queries
# JOIN Version = 1 query

SELECT * FROM enrollments;
SELECT first_name, last_name
FROM students
WHERE student_id = 3;

SELECT first_name, last_name
FROM students
WHERE student_id = 4;

SELECT first_name, last_name
FROM students
WHERE student_id = 5;

-- Task 3: N+1 Problem

-- Bad Approach (N+1):
-- Query 1:
SELECT * FROM enrollments;

-- Then for each enrollment:
SELECT first_name, last_name
FROM students
WHERE student_id = ?;

-- Total Queries:
-- 1 + N

-- Current database:
-- N = 10 enrollments
-- Total = 11 queries

-- Optimized Approach:
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

-- Total Queries = 1

-- If database contains 10,000 enrollments:
-- N+1 approach = 10,001 queries
-- JOIN approach = 1 query
