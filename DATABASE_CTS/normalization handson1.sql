-- 1NF:
-- All columns contain atomic values.
-- No column stores multiple values.
-- Example violation: storing multiple phone numbers in one column.

-- 2NF:
-- Every non-key attribute depends on the entire primary key.
-- In enrollments, enrollment_date and grade depend on the enrollment record.

-- 3NF:
-- No transitive dependencies exist.
-- Department details are stored in departments table.
-- Storing dept_name in students would violate 3NF.
-- Enrollments stores only enrollment-related data.