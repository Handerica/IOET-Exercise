with open('schedule.txt') as file:
    l_employees = file.readlines()
    l_employees = [emp.strip() for emp in l_employees]


for i in range(len(l_employees)):
    for j in range(i+1, len(l_employees)):
        if l_employees[i].split('=')[0] != l_employees[j].split('=')[0]:
            name_1, name_2 = l_employees[i].split('=')[0], l_employees[j].split('=')[0]
            sched1, sched2 = l_employees[i].split('=')[1], l_employees[j].split('=')[1]
            l_sched1, l_sched2 = sched1.split(','), sched2.split(',')
            cont_sched = 0
            for day1 in l_sched1:
                for day2 in l_sched2:
                    if day1[0:2] == day2[0:2]:
                        init_hour1 = day1[2:].split('-')[0]
                        end_hour1 = day1[2:].split('-')[1]
                        init_hour2 = day2[2:].split('-')[0]
                        end_hour2 = day2[2:].split('-')[1]

                        f_init_hour1 = int(init_hour1.split(':')[0].strip()) + int(init_hour1.split(':')[1].strip()) * (1/60)
                        f_end_hour1 = int(end_hour1.split(':')[0].strip()) + int(end_hour1.split(':')[1].strip()) * (1/60)
                        f_init_hour2 = int(init_hour2.split(':')[0].strip()) + int(init_hour2.split(':')[1].strip()) * (1/60)
                        f_end_hour2 = int(end_hour2.split(':')[0].strip()) + int(end_hour2.split(':')[1].strip()) * (1/60)

                        if init_hour2 <= init_hour1 <= end_hour2 or init_hour2 <= end_hour1 <= end_hour2:
                            cont_sched += 1
                        
            print(f'{name_1} - {name_2}: {cont_sched}')
