# Timetable auto project

To reduce college students' timetable aranging time from **30 minutes** to **10 seconds**.

## 1. Context
Every semester, students in universities in Vietnam has to choose what course to sign up for. Each course has different classes, with different time. Eg: Course code TMA404, class code TMA404.1

![This is an image](/img/tma404.png)

Students have to do these  steps manually:
- (1) Choose course codes. (Eg: MKT407, KTE312, TMA404,...)
- (2) List all class for each course. (Eg: MKT407.1, MKT407.2, KTE312.2,...)
- (3) Pick a class A for first course.
- (4) Pick a class B for second course, not overlapping class A time, if not possible, redo step 3.
- (5) Pick a class C for third course, not overlapping class A and class B time. If not possible, redo step 4. If not possible, redo step 3.
- (6) ...

The complexity of this 'manual' algorithm can be varied due to number of classes opened, number of courses students wish to sign up,...

## 2. Solution
Create a program, take the input of a list of course code students wish to sign up for, then return the output of all possible timetable.
- Input: ['MKT407', 'KTE312', 'TMA404', 'KTE319', 'TMA311']
- Output:
![This is an image](/img/output.png)

## 3. Efficiency
This process used to take up to 30 minutes, now it is only 10 seconds.