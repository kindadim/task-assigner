import random

def read_file_to_list(filename):
    with open(filename, 'r') as file:
        # Splits list by new line
        file_list = file.read().splitlines()
        # Remove empty strings from list
        file_list = [x for x in file_list if x] 
        return file_list

def shuffle_list(file_list):
    # Shuffles list to prevent bias
    random.shuffle(file_list)
    return file_list

class Person:
    # This method is called when the object is created
    # It sets the attributes of the object
    # Parameters:
    #   name: The name of the person
    #   Weight: The weight of the person (used for sorting, this is the priority)
    #   task: The task of the person
    def __init__(self, name, Weight, task):
        self.name = name
        self.Weight = Weight
        self.task = task

    # This method is called when the object is converted to a string
    # It returns the string representation of the object
    # This is useful for printing
    def __str__(self):
        return f'{self.name} {self.task}'

    # This method is called when the object is printed
    # It returns the string representation of the object
    # This is useful for debugging
    def __repr__(self):
        return f'{self.name} {self.task}'

def assign_task():
    # Reads people.txt and converts it to a list, sort it by the last character (int) and reverse it
    people_list = sorted(read_file_to_list('./Config/Titles.txt'), key=lambda x: int(x[-2:]), reverse=True)
    
    # Reads tasks.txt and converts it to a list
    task_list = shuffle_list(read_file_to_list('./Config/Tasks.txt'))

    # zip both shuffled lists together
    zipped_list = zip(people_list, task_list)
    for person, task in zipped_list:
        # Create a person object
        #                        name,       weight,    task
        PersonObject = Person(person[:-1], person[-2:], task)
        # Note that the field PersonObject.Weight is not used, it is still there.
        print(f'Name: {PersonObject.name} |> Task: {PersonObject.task}')


# This is the main function
# It is called when the file is run
if __name__ == '__main__':
    assign_task()