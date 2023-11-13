import random

assigned = []
unassigned = []
to_print = ''
file_write = ''


def assign_people(filename, task_count):
    global assigned, unassigned
    with open(filename, 'r') as file:
        read_values = file.read()
        read_values = read_values.splitlines()
        random.shuffle(read_values)
        read_values.sort(reverse=True, key=lambda v: v.split()[-1])
        assigned += read_values[:task_count]
        unassigned += read_values[task_count:]
    return


def assign_tasks(tasks):
    global assigned, unassigned, to_print, file_write
    random.shuffle(tasks)
    cycle = 0

    for person in assigned:
        task = tasks[cycle]
        person = person.split()
        to_print += '{} - {}\n'.format(person[:-1], task)
        file_write += '{} 0\n'.format(person[:-1])
        cycle += 1

    for person in unassigned:
        last_time_assigned = (person[-1:])
        person = person[:-1]
        file_write += '{}{}\n'.format(person, int(last_time_assigned) + 1)
    return


def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(file_write)
    return


assign_people('Shuffler/Config/Titles.txt', 5)
assign_tasks(['Sweeping', 'Garbage', 'Surfaces', 'Vacuuming', 'Bathroom'])
write_to_file('Shuffler/Config/Titles.txt')

print(to_print)