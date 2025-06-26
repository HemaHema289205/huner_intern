CREATE TABLE Student(RollNo INT PRIMARY KEY,Name VARCHAR(100),Marks INT,Aadhar VARCHAR(12) UNIQUE,Address VARCHAR(255));
CREATE TABLE Course(RollNo INT,Course VARCHAR(100),Course_Duration VARCHAR(50),FOREIGN KEY (RollNo) REFERENCES Student(RollNo));

INSERT INTO Student VALUES(201,'Kavya',91,'111122223333','vizag'),(202,'Nikhil',84,'444455556666','vijayawada'),
                          (203,'Hema',28,'111144443333','Eluru'),(204,'Madhu',75,'333455556666','vijayawada'),
                          (205,'Lokesh',30,'111144442222','Kakinada'),(206,'Dakshith',50,'333488886666','Puna'),
                          (207,'Rakshith',50,'333455886666','Puna');
INSERT INTO Course VALUES(201,'Data Science','6 Months'),(201,'SQL','3 Months'),(202,'Python','4 Months'),
                         (203,'Aritificial Intelligence','6 Months'),(201,'SQL','3 Months'),(204,'Java','4 Months'),
                         (207,'BCA','6 Months'),(201,'BCA','3 Months'),(202,'Python','4 Months');



SELECT AVG(Marks) AS Marks FROM Student;

SELECT * FROM Student ORDER BY Name ASC;

SELECT RollNo, Name FROM Student WHERE Marks <30;

SELECT  Name FROM Student WHERE Name LIKE 'R%';

SELECT s.RollNo,s.Name FROM Student s JOIN Course c ON s.RollNo = c.RollNo WHERE c.Course='BCA';
