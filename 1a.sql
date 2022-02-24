SELECT Name, Total_marks
FROM name_table  NT JOIN mark_table MT ON NT.StudentID = MT.StudentID
WHERE Total_marks > (
    SELECT Total_marks FROM mark_table WHERE StudentID = 'V002'
);