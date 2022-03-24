# IOET-Exercise

## Exercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:

ASTRID-RENE: 2

ASTRID-ANDRES: 3

RENE-ANDRES: 2



Example 2:

INPUT:

RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:

RENE-ASTRID: 3

Once you have finished the exercise, please upload the solution to GitHub and send us the link. Don’t forget to include a README.md file. Your README should include an overview of your solution, an explanation of your architecture, an explanation of your approach and methodology and instructions how to run the program locally.

We evaluate many aspects, including how well your code is structured, applied pattern designs, testing and the quality of your solution.

The solution shouldn’t need any UI, a console application is good enough.

When submitting your exercise, be sure to avoid including compiled files as this could be considered malware. Please include the proper instructions to compile your project in the README file

This exercise should be completed within a week. If for some reason you are unable to finish on time, please let us know.



## Overview
Based on the given data, the proposed solution is to make a list where each element is a row from the txt file, but also that line represented the information from an employee and it's working hours with the format 'name=schedule'.

Then iterate over that list and comparing each element ONLY with the elements at their right side of the list to get all the possible, non-repeatable, combinations of pairs of employees.

From those combinations obtained, in the previous steps, it is needed to manipulate the string from the schedule by using substrings and the split method in order to separate the day from the working hours and validate if the employees worked the same day.

The following step is to validate if the working hours of a pair of employees intersect and to do so, the string that represents an hour is converted to it's equal in decimal numerical system to compare values.

Finally, it is applied that if the initial hour from an employee was in the range of the initial and end hour from the second employee or vice versa then the schedule of those two employees intersects in that specific day.



## Methodology
Based on the input it is needed to sort the data into a list that contains the information of an employee in each specific element and then compare to each other without repeating the employees, this means to find all the possible combinations but NOT the permutations.
For example: 'Hugo - Rene' combination is the same as 'Rene - Hugo' since both refer to the same employees.

After analyzing the distribution of the data, it is concluded that to obtain all the possible combinations without repeating an iteration from left to right needs to be done but with the restriction of comparing each element only with the elements that are in the same direction of the iteration order, in this case the ones at the right side. 

Once the combinations are obtained, we can identify the structure of each element from the list, shown as follows:
- 'Name=Day(1)InitHour(1)-EndHour(1), Day(2)InitHour(2)-EndHour(2), ..., Day(n)InitHour(n)-EndHour(n)'

where InitHour is divides in minutes as shown:
- InitHour = 'Hours:Minutes'

So, it is visible that: 
- The name and the schedule are separated with '='
- Each working day with it schedule is separated by ','
- Each day is always represented by 2 characters (MO, TU, WE, TH, FR, SA, SU).
- The initial hour and the ending hour are separated by ':'

Once identified all the separators substrings and the split method are used to get values needed. First comparing if the pair of employees worked the same day and if they did then compare if the initial hour OR the ending hour of one of them are in the range of the initial and ending hour of the second one. if that is true then that means that they worked in the same day and intersecting their schedules then a counter increases by one. After comparing each couple of employees, it is shown on screen the combination of employees and their schedule intersections.



## To run the code
1. Clone the repository
2. Make sure that the file "schedule.txt" is in the same folder as "exercise.py" python file.
3. The user is able to add or delete data from the "schedule.txt" file but keeping the same format as the other rows.
3. Run the code from your IDE, text editor or just from terminal.
