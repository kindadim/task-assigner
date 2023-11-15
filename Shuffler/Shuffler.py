import random


def read_file(file_name):
    with open(file_name, 'r') as file:
        file_list = []
        line_count = 0
        for line in file:
            read_list = line.splitlines()
            read_list = [x for x in read_list if x]
            file_list += read_list
            line_count += 1
            continue
    return file_list, line_count
# Returns file_list and line_count
def shuffler(file_list):
    random.shuffle(file_list)
    return file_list
# Returns shuffled file_list
def task_list(task_file):
    tasks, task_count = shuffler(read_file(task_file)[0]), (read_file(task_file)[1])
    return tasks, task_count
# Returns tasks and task_count
def title_list(title_file):
    titles = shuffler(read_file(title_file)[0])
    titles.sort(reverse=True, key=lambda v: v.split()[-1]) # Orders titles by integer
    return titles
# Returns titles
def zipper(titles, tasks, task_count):
    to_file = ''
    assigned = zip(titles, tasks)
    for title, task in assigned:
        name = title[:-2]
        print(f'{name} - {task}')
        to_file += (f'{name} 0\n')
        continue
    unassigned = titles[task_count:]
    for title in unassigned:
        name, weight = title[:-2], int(title[-1])
        weight = weight + 1
        to_file += (f'{name} {weight}\n')
        continue
    return to_file
# Prints readable data, returns data to be written to file
def file_updater(title_file, to_file):
    with open(title_file, 'w') as file:
        file.write(to_file)
    return

task_file = 'Shuffler/Config/Tasks.txt'
title_file = 'Shuffler/Config/Titles.txt'
#print(task_list(task_file)) # For troubleshooting
#print(title_list(title_file)) # For troubleshooting
#zipper(title_list(title_file), task_list(task_file)[0], task_list(task_file)[1]) # For troubleshooting

file_updater(title_file, zipper(title_list(title_file), task_list(task_file)[0], task_list(task_file)[1]))