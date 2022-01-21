from ast import Try
import sys
import clipboard
import json

#print whatever there is on the clipboard
# data = clipboard.paste()
# print(data)

#copy anything to the clip board, here itcopies Thank you to the clipboard
# clipboard.copy("Thank you")

SAVED_DATA = "Clipboard.json"
'''
A function that saves items fed as argument to a json file if it exists, else creates a new file and writes
the data in it
'''
def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)
        
'''
Read and load the JSON file and convert into dictionary
'''
def load_data(filename):
    try:
        with open(filename, 'r') as f:
            dict = json.load(f)
            return dict
    except:
        return {}
        

if len(sys.argv) == 2:
    
    '''
    argv are the arguments passed when the programs is run 
    
    for example: in the command "python multiclipboard.py list" all the words except python are the arguments
    passed when the terminal executes the python file. Here sys.argv is the list of all such arguments. 
     This list can be sliced, and behaves as normal list.
    '''
   
    command = sys.argv[1]  
    '''
    getting data from the file
    '''
    data = load_data(SAVED_DATA)
    if command == "save":
        key = input("Enter a Key to save whatever is there on clipboard")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    elif command == "load":
        key = input("Enter a Key to save whatever is there on clipboard")
        if key in data:
            clipboard.copy(data[key])
            print("Copied to Clipboard")
        else:
            print("Key Not Found!")
    elif command == "list":
        print(data)
    else:
        print("Command not recognised!!")
else:
    print("please pass one good command")