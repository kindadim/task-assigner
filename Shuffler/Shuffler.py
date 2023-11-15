import random

def read_file(file_name): # Opens a file, returns a list of lines and line count
    with open(file_name, 'r') as file:
        file_list = []
        line_count = 0
        for line in file:
            read_list = line.splitlines()
            read_list = [x for x in read_list if x] # Removes empty strings
            file_list += read_list # Adds lines to a list
            line_count += 1 # Counts the number of lines iterated through
            continue
    return file_list, line_count
# Returns file_list and line_count
def shuffler(file_list): # A funny lil shuffle
    random.shuffle(file_list)
    return file_list
# Returns a shuffled list
def task_list(task_file): # Uses read_file() and shuffler() on the task_file
    tasks, task_count = shuffler(read_file(task_file)[0]), (read_file(task_file)[1])
    return tasks, task_count
# Returns shuffled tasks and task_count
def title_list(title_file): # Uses read_file() and shuffler() on the title_file, and orders titles by weight
    titles = shuffler(read_file(title_file)[0]) # Takes only file_list from read_file() and shuffles it
    titles.sort(reverse=True, key=lambda v: v.split()[-1]) # Orders titles by weight
    return titles
# Returns shuffled/sorted titles
def zipper(titles, tasks, task_count): # Zips titles/tasks, resets/adds weight, refactors titles
    to_file = ''
    assigned = zip(titles, tasks) # Zips the assigned titles and tasks together
    for title, task in assigned:
        name = title[:-2] # Removes the weight for printing and resetting weight
        print(f'{name} - {task}') # Prints titles and the task assigned to them in a readable format
        to_file += (f'{name} 0\n') # Resets weight to 0 and appends to the to_file variable
        continue
    unassigned = titles[task_count:] # Grabs only the unzipped titles
    for title in unassigned:
        name, weight = title[:-2], int(title[-1]) # Splits the title into name and weight
        weight = weight + 1 # Weight gets 1 added
        to_file += (f'{name} {weight}\n') # Recombines name and weight and appends to the to_file variable
        continue
    return to_file
# Prints readable data, returns to_file to be written to title_file
def file_updater(title_file, to_file): # Writes to_file to the title_file
    with open(title_file, 'w') as file:
        file.write(to_file)
    return

task_file = 'Shuffler/Config/Tasks.txt' # task_file, where task names are stored
title_file = 'Shuffler/Config/Titles.txt' # title_file, where name and weight are stored
#print(task_list(task_file)) # For troubleshooting
#print(title_list(title_file)) # For troubleshooting
#zipper(title_list(title_file), task_list(task_file)[0], task_list(task_file)[1]) # For troubleshooting

file_updater(title_file, zipper(title_list(title_file), task_list(task_file)[0], task_list(task_file)[1]))