import random

def assign_tasks(task_file, title_file):
    assigned = [] # List of people to be assigned tasks
    unassigned = [] # List of people not assigned tasks
    titles = [] # List of titles - shuffled and sorted
    tasks = [] # List of tasks - shuffled
    to_zip = ''
    to_file = ''
    to_print = ''
    task_count = 0 # Number of tasks
    
    with open(task_file, 'r') as taskfile: # Opens task_file
        for task in taskfile: # Iterates through each line
            tasks += task.split('\n') # Splits list by new line
            tasks = [x for x in tasks if x] # Removes empty strings
            random.shuffle(tasks) # Shuffles tasks to prevent bias
            task_count += 1 # Counts the tasks iterated through
            continue
    
    with open(title_file, 'r') as titlefile: # Opens title_file
        for title in titlefile: # Iterates through each line
            titles += title.splitlines() # Splits list by new line
            titles = [x for x in titles if x] # Removes empty strings
            random.shuffle(titles) # Shuffles titles to prevent bias
            titles.sort(reverse=True, key=lambda v: v.split()[-1]) # Orders titles by integer
            continue

        assigned += titles[:task_count] # Splits titles by who will be assigned
        for person in assigned:
            person = person[:-1] # Removes the integer
            to_file += str(person) + '0\n' # Resets the integer to send to file
            to_print += str(person)
        
        zipped_list = list(zip(assigned, tasks))
        
        unassigned += titles[task_count:]
        for person in unassigned:
            oldtime = person[-1]
            newtime = int(oldtime) + 1
            person = person[:-1] + str(newtime)
            to_file += str(person) + '\n'
            continue

    return zipped_list
    
print(assign_tasks('Shuffler/Config/Tasks.txt', 'Shuffler/Config/Titles.txt')) # prints and assigns filenames