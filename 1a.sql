-- returns the name and student ID of all students 
--that have a higher total marks score
--than the student that has StudentID of 'V002’
SELECT Name, Total_marks
FROM name_table  NT JOIN mark_table MT ON NT.StudentID = MT.StudentID
WHERE Total_marks > (
    SELECT Total_marks FROM mark_table WHERE StudentID = 'V002'
);