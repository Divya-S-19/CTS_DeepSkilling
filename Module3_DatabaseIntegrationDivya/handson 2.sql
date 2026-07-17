-- Task 1 HANDSON2 
DESC departments;
INSERT INTO departments (dept_name, head_of_dept, budget)
VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);
SELECT * FROM departments;

INSERT INTO students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
VALUES
('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022),
('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022),
('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021),
('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023),
('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022),
('Kavya', 'Menon', 'kavya.menon@college.edu', '2002-05-17', 2, 2021),
('Aditya', 'Singh', 'aditya.singh@college.edu', '2004-03-22', 4, 2023),
('Deepika', 'Rao', 'deepika.rao@college.edu', '2003-08-09', 1, 2022);
SELECT COUNT(*) FROM students;

INSERT INTO courses (course_name, course_code, credits, department_id)
VALUES
('Data Structures & Algorithms', 'CS101', 4, 1),
('Database Management Systems', 'CS102', 3, 1),
('Object Oriented Programming', 'CS103', 4, 1),
('Circuit Theory', 'EC101', 3, 2),
('Thermodynamics', 'ME101', 3, 3);
SELECT COUNT(*) FROM courses;

DESC enrollments;
SELECT student_id, first_name, last_name
FROM students;

SELECT COUNT(*) FROM enrollments;
SELECT course_id, course_name
FROM courses;
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES
(3, 1, '2022-07-01', 'A'),
(3, 2, '2022-07-01', 'B'),
(4, 1, '2022-07-01', 'B'),
(4, 3, '2022-07-01', 'A'),
(5, 4, '2021-07-01', 'A'),
(6, 5, '2023-07-01', NULL),
(7, 1, '2022-07-01', 'C'),
(7, 2, '2022-07-01', 'A'),
(8, 4, '2021-07-01', 'B'),
(9, 5, '2023-07-01', NULL),
(10, 1, '2022-07-01', 'A'),
(10, 3, '2022-07-01', 'B');
SELECT COUNT(*) AS total_enrollments
FROM enrollments;
INSERT INTO professors (prof_name, email, department_id, salary)
VALUES
('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00),
('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00),
('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00),
('Dr. Latha Gopal', 'latha.g@college.edu', 3, 79000.00),
('Dr. Kartik Bose', 'kartik.b@college.edu', 4, 76000.00);
SELECT COUNT(*) AS total_professors
FROM professors;
INSERT INTO students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
VALUES
('Rahul', 'Kumar', 'rahul.kumar@college.edu', '2003-05-10', 1, 2022),
('Anjali', 'Sharma', 'anjali.sharma@college.edu', '2004-02-15', 2, 2023);
SELECT COUNT(*) AS total_students
FROM students;
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM enrollments;
SELECT COUNT(*) FROM professors;
UPDATE enrollments
SET grade = 'B'
WHERE student_id = 7
AND course_id = 1;
SELECT *
FROM enrollments
WHERE grade IS NULL;
DELETE FROM enrollments
WHERE grade IS NULL;
SET SQL_SAFE_UPDATES = 0;
DELETE FROM enrollments
WHERE grade IS NULL;
SELECT COUNT(*) FROM enrollments;

-- TASK 2 HANDSON2
SELECT *
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name ASC;
SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;
SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;
SELECT *
FROM students
WHERE email LIKE '%@college.edu';
SELECT
enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year;

-- TASK 3 HANDSON 2
SELECT
CONCAT(s.first_name,' ',s.last_name) AS student_name,
d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

SELECT
e.enrollment_id,
CONCAT(s.first_name,' ',s.last_name) AS student_name,
c.course_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

SELECT
s.student_id,
s.first_name,
s.last_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

SELECT
c.course_name,
COUNT(e.student_id) AS enrolled_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT
d.dept_name,
p.prof_name,
p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id;

-- TASK 4 HANDSON 2

SELECT
c.course_name,
COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT
d.dept_name,
ROUND(AVG(p.salary),2) AS avg_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

SELECT *
FROM departments
WHERE budget > 600000;

SELECT
grade,
COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY grade;

SELECT
d.dept_name,
COUNT(DISTINCT s.student_id) AS student_count
FROM departments d
JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(DISTINCT s.student_id) > 2;