"""Shuffle randomizes lists"""
from random import shuffle


def read_file(file_name):
    """Opens a file, returns a list of lines and line count"""
    with open(file_name, 'r', encoding='utf-8') as file:
        file_list = []
        line_count = 0
        for line in file:
            read_list = line.splitlines()
            read_list = [x for x in read_list if x]
            file_list += read_list
            line_count += 1
            continue
    return file_list, line_count

def shuffler(file_list):
    """A funny little shuffle"""
    shuffle(file_list)
    return file_list

def task_list(task_file):
    """Uses read_file() and shuffler() on the task_file"""
    tasks, task_count = shuffler(read_file(task_file)[0]), (read_file(task_file)[1])
    return tasks, task_count

def title_list(title_file):
    """Uses read_file() and shuffler() on the title_file, and orders titles by weight"""
    titles = shuffler(read_file(title_file)[0])
    titles.sort(reverse=True, key=lambda v: v.split()[-1])
    return titles

def zipper(titles, tasks, task_count):
    """Zips titles/tasks, resets/adds weight, refactors titles"""
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

def file_updater(title_file, task_file):
    """Writes to_file to the title_file"""
    to_file = zipper(title_list(title_file), task_list(task_file)[0], task_list(task_file)[1])
    with open(title_file, 'w', encoding='utf-8') as file:
        file.write(to_file)


file_updater(
    'shuffler/config/titles.txt', 
    # File containing name and assignment weight
    'shuffler/config/tasks.txt') 
    # File containing tasks
