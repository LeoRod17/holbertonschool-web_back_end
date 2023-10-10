all tasks of the proyect
Leter of the exercise:
content

line to test: the command

task 0
0-Basic list of objecs:
Create a function named getListStudents that returns an array of objects.
Each object should have three attributes: id (Number), firstName (String), and location (String).
The array contains the following students in order:
Guillaume, id: 1, in San Francisco
James, id: 2, in Columbia
Serena, id: 5, in San Francisco
line to test: npm run dev 0-main.js

Task 1:
1-More mapping
Create a function getListStudentIds that returns an array of ids from a list of object.
This function is taking one argument which is an array of objects - and this array is the same format as getListStudents from the previous task.
If the argument is not an array, the function is returning an empty array.
You must use the map function on the array.
line to test: npm run dev 1-main.js

Task 2:
2-Filter
Create a function getStudentsByLocation that returns an array of objects who are located in a specific city.
It should accept a list of students (from getListStudents) and a city (string) as parameters.
You must use the filter function on the array.
line to test: npm run dev 2-main.js

Task 3:
3-Reduce
Create a function getStudentIdsSum that returns the sum of all the student ids.
It should accept a list of students (from getListStudents) as a parameter.
You must use the reduce function on the array.
line to test: npm run dev 3-main.js 

Task 4:
4-Combine
Create a function updateStudentGradeByCity that returns an array of students for a specific city with their new grade
It should accept a list of students (from getListStudents), a city (String), and newGrades (Array of “grade” objects) as parameters.

newGrades is an array of objects with this format:
  {
    studentId: 31,
    grade: 78,
  }

If a student doesn’t have grade in newGrades, the final grade should be N/A.
You must use filter and map combined.
line to test: npm run dev 4-main.js

Task 5:
5-Typed Arrays
Create a function named createInt8TypedArray that returns a new ArrayBuffer with an Int8 value at a specific position.
It should accept three arguments: length (Number), position (Number), and value (Number).
If adding the value is not possible the error Position outside range should be thrown.
line to test: npm run dev 5-main.js

Task 6:
6-Set data structure
Create a function named setFromArray that returns a Set from an array.
It accepts an argument (Array, of any kind of element).
line to test: npm run dev 6-main.js 

Task 7:
7-More set data structure
Create a function named hasValuesFromArray that returns a boolean if all the elements in the array exist within the set.
It accepts two arguments: a set (Set) and an array (Array).
line to test: npm run dev 7-main.js

Task 8:
8-Clean set
Create a function named cleanSet that returns a string of all the set values that start with a specific string (startString).
It accepts two arguments: a set (Set) and a startString (String).
When a value starts with startString you only append the rest of the string. The string contains all the values of the set separated by -.
line to test: npm run dev 8-main.js 

Task 9:
9-Map data structure
Create a function named groceriesList that returns a map of groceries with the following items (name, quantity):

Apples, 10
example
Tomatoes, 10
Pasta, 1
Rice, 1
Banana, 5
line to test: npm run dev 9-main.js

Task 10:
10 -More map data structure
Create a function named updateUniqueItems that returns an updated map for all items with initial quantity at 1.
It should accept a map as an argument. The map it accepts for argument is similar to the map you create in the previous task.
For each entry of the map where the quantity is 1, update the quantity to 100. If updating the quantity is not possible (argument is not a map) the error Cannot process should be thrown.
line to test: npm run dev 10-main.js
---------------------------------------- end  of Tasks --------------------------------------------------