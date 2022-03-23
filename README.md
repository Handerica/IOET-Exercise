# IOET-Exercise

## Overview
Based on the given data, the proposed solution is to make a list where each element is a row from the txt file, but also that line represented the information from an employee and it's working hours with the format 'name=schedule'.

Then iterate over that list and comparing each element ONLY with the elements at their right side of the list to get all the possible, non-repeatable, combinations of pairs of employees.

From those combinations obtained, in the previous steps, it is needed to manipulate the string from the schedule by using substrings and the split method in order to separate the day from the working hours and validate if the employees worked the same day.

The following step is to validate if the working hours of a pair of employees intersect and to do so, the string that represents an hour is converted to it's equal in decimal numerical system to compare values.

Finally, it is applied that if the initial hour from an employee was in the range of the initial and end hour from the second employee or vice versa then the schedule of those two employees intersects in that specific day.


## Methodology
Based on the input it is needed to sort the data into a list that contains the information of an employee in each specific element and then compare to each other without repeating the employees, this means to find all the possible combinations but NOT the permutations.
For example: 'Hugo - Rene' combination is the same as 'Rene - Hugo' since both reffer to the same employees.

After analyzing the distribution of the data it is consluded that in order to obtain all the possible combinations without repeating an iteration from left to right needs to be done but with the restriction of comparing each elements only with the elements that are in the same direction of the iteration order, in this case the ones at the right side. 

Once the combinations are obtained we can identify the structure of each element from the list, shown as follows:
'Name=Day[_1]1InitHour1-EndHour1, Day2InitHour2-EndHour2, ..., DaynInitHourn-EndHourn'


## To run the code
1. Clone the repository
2. Make sure that the file "schedule.txt" is in the same folder as "exercise.py" python file.
3. The user is able to add or delete data from the "schedule.txt" file but keeping the same format as the other rows.
3. Run the code from your IDE, text editor or just from terminal.
