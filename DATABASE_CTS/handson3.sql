-- Task 1 handson 3
SELECT s.student_id,
       s.first_name,
       s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(*) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_table
);

SELECT s.student_id,
       s.first_name,
       s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(*) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) avg_table
);
SELECT p.*
FROM professors p
WHERE salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

SELECT *
FROM
(
    SELECT department_id,
           AVG(salary) AS avg_salary
    FROM professors
    GROUP BY department_id
) dept_avg
WHERE avg_salary > 85000;

-- Task 2 handson 3 
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN grade='A' THEN 4
                WHEN grade='B' THEN 3
                WHEN grade='C' THEN 2
                WHEN grade='D' THEN 1
                WHEN grade='F' THEN 0
            END
        ),2
    ) AS GPA
FROM students s
LEFT JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY s.student_id, student_name, d.dept_name;

SELECT * FROM vw_student_enrollment_summary;
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN grade='A' THEN 4
                WHEN grade='B' THEN 3
                WHEN grade='C' THEN 2
                WHEN grade='D' THEN 1
                WHEN grade='F' THEN 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_id,c.course_name,c.course_code;

SELECT * FROM vw_course_stats;

SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3.0;

UPDATE vw_student_enrollment_summary
SET GPA = 4
WHERE student_id = 3;

DROP VIEW vw_student_enrollment_summary;
DROP VIEW vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id
FROM students
WHERE department_id = 1
WITH CHECK OPTION;

SELECT * FROM vw_student_enrollment_summary;

-- Task 3 handson 3

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    IF EXISTS (
        SELECT *
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    )
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Duplicate enrollment not allowed';
    ELSE
        INSERT INTO enrollments
        (student_id,course_id,enrollment_date,grade)
        VALUES
        (p_student_id,p_course_id,p_enrollment_date,NULL);
    END IF;

END$$

DELIMITER ;
CALL sp_enroll_student(3,5,'2024-01-01');

CREATE TABLE department_transfer_log(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN

    DECLARE v_old_department INT;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id=p_student_id;

    UPDATE students
    SET department_id=p_new_department
    WHERE student_id=p_student_id;

    INSERT INTO department_transfer_log
    (student_id,old_department,new_department)
    VALUES
    (p_student_id,v_old_department,p_new_department);

    COMMIT;

END$$

DELIMITER ;

CALL sp_transfer_student(3,999);
SELECT *
FROM students
WHERE student_id=3;

START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(3,5,CURDATE(),NULL);

SAVEPOINT first_insert;

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(999,5,CURDATE(),NULL);

ROLLBACK TO first_insert;

COMMIT;
SELECT *
FROM enrollments
WHERE student_id=3
AND course_id=5;