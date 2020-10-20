import glob
import os
import random

def renameFilesToRandomOrder(extension: str, number_of_files: int):

    list = []
    total = []

    for _ in range(number_of_files * 2):
        # create list with random numbers 2 times larger than the number of files
        random_number = random.randint(0, 1000)
        list.append(random_number)

    for number in list:
        if total.count(number) == 0:
        # verify if the number in list is in the total array
            total.append(number)
    cont = 0
    for file in glob.glob(f'*.{extension}'):
        # get all files with the current
        # extension and rename them with the numbers in total array
        new_filename = file.replace(file[:-(len(extension)+1)], str(total[cont]))
        os.rename(file, new_filename)
        print(new_filename)
        cont += 1


if __name__ == '__main__':
    renameFilesToRandomOrder("txt", 12)
