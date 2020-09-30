import pickle
from modules.colours import *

def add_data(extensions):
    cyan("\nCategories : ")
    for ex in extensions:
        print("\t• " + ex)
    category = input("\nWhich category does the extension belong to? (Type the exact name)\n> ").capitalize()
    new_extension = input("Enter the extension you want to add. Eg: EXE,PNG,JPEG\n> ")
            
    new_extension = ("." + new_extension)
    try:
        extensions[category].append(new_extension)
        pickle_file = open("../assets/extensions_data.pkl", 'wb')
        pickle.dump(extensions, pickle_file)
        pickle_file.close()   
        green("\nExtension has been added")
    except:
        red("\nERROR : CATEGORY DOES NOT EXIST")


def add_category(extensions):
    key = input("\nEnter the new category to be added\n> ").capitalize() 
    value = input("Enter the extension\n> ")
    value = ("." + value)
    extensions[key] = [value]

    pickle_file = open("../assets/extensions_data.pkl", 'wb')
    pickle.dump(extensions, pickle_file)
    pickle_file.close()
            
    green("\nExtension has been added")


def delete_data(extensions):
    cyan("\nCategories : ")
    for ex in extensions:
        print("\t• " + ex)

    category = input("\nWhich category does the extension belong to? (Type the exact name)\n> ").capitalize()
    try:
        cyan("\nExtensions : ")
        for y in range(len(extensions[category])):
            print("\t->",extensions[category][y])

        del_extension = input("\nEnter the extension you want to delete. Eg: EXE,PNG,JPEG\n> ")
        del_extension = ("." + del_extension)
        extensions[category].remove(del_extension)

        if(extensions[category] == []):
            extensions.pop(category)

        pickle_file = open("../assets/extensions_data.pkl", 'wb')
        pickle.dump(extensions, pickle_file)
        pickle_file.close()
        green("\nExtension has been Deleted!")
    except:
        red("\nERROR : CATEGORY DOES NOT EXIST")
        

def view_data(extensions):
    cyan("\nCategories : ")
    for ex in extensions:
        print("\t• " + ex)
    category = input("\nWhich category does the extension belong to? (Type the exact name)\n> ").capitalize()
    try:
        cyan("\nExtensions : ")
        for y in range(len(extensions[category])):
            print("\t->",extensions[category][y])
    except:
        red("\nERROR : CATEGORY DOES NOT EXIST")
