import random

assigned = []
unassigned = []
task_count = ''
to_print = ''
to_file = ''


def assign_tasks(tasks_file):
    global assigned, unassigned, to_print, to_file
    with open(tasks_file, 'r') as file:
        read_tasks = file.read()
        tasks = read_tasks.splitlines()
        random.shuffle(tasks)

    cycle = 0
    for person in assigned:
        task = tasks[cycle]
        person = person.split()
        to_print += task + ' - ' + ' '.join(map(str, person[:-1])) + '\n'
        to_file += ' '.join(map(str, person[:-1])) + ' 0' '\n'
        cycle += 1

    for person in unassigned:
        last_time_assigned = (person[-1:])
        person = person[:-1]
        to_file += '{}{}\n'.format(person, int(last_time_assigned) + 1)
    return

def assign_people(titles_file, task_count):
    global assigned, unassigned
    with open(titles_file, 'r') as file:
        read_titles = file.read()
        split_titles = read_titles.splitlines()
        random.shuffle(split_titles)
        split_titles.sort(reverse=True, key=lambda v: v.split()[-1])
        assigned += split_titles[:task_count]
        unassigned += split_titles[task_count:]
    return

def write_to_file(titles_file):
    with open(titles_file, 'w') as file:
        file.write(to_file)
    return


assign_people('Shuffler/Config/Titles.txt', 11)
assign_tasks('Shuffler/Config/Tasks.txt')
write_to_file('Shuffler/Config/Titles.txt')

print(to_print)