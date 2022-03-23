# IOET-Exercise

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
'Name=Day(1)InitHour(1)-EndHour(1), Day(2)InitHour(2)-EndHour(2), ..., Day(n)InitHour(n)-EndHour(n)'

where InitHour is divides in minutes as shown:
InitHour = 'Hours:Minutes'

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
