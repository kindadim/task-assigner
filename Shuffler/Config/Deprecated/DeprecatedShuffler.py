import random

def assign_tasks(titles_file, tasks_file):
    assigned = []
    unassigned = []
    task_count = 0
    to_file = ''

    with open(tasks_file, 'r') as taskfile:
        taskfile = taskfile.strip()
        read_tasks = taskfile.readlines()
        tasks = ''.join(read_tasks)
        task_count = len(read_tasks)
        random.shuffle(read_tasks)
        

    with open(titles_file, 'r') as titlefile:
        split_titles = titlefile.read().splitlines()
        random.shuffle(split_titles)
        split_titles.sort(reverse=True, key=lambda v: v.split()[-1])
        assigned += split_titles[:task_count]
        assigned_list = list(zip(assigned, read_tasks))
        to_file += str(assigned_list)

        unassigned += split_titles[task_count:]
        for person in unassigned:
            last_time_assigned = (person[-1:])
            person = person[:-1]
            to_file += '{}{}\n'.format(person, int(last_time_assigned) + 1)

    with open(titles_file, 'w') as file:
        file.write(to_file)
    return read_tasks



print(assign_tasks('Shuffler/Config/Titles.txt', 'Shuffler/Config/Tasks.txt'))