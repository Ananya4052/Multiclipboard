import clipboard
import json
import os
import sys
data_file = "clipboard.json"
def save(key, data):
    with open(data_file, 'r+') as f:
        try:
            data_dict = json.load(f)
        except ValueError:
            data_dict = {}
        data_dict[key] = data
        f.seek(0)
        json.dump(data_dict, f)
        f.truncate()
def load(key):
    with open(data_file, 'r+') as f:
        try:
            data_dict = json.load(f)
        except ValueError:
            print("No data saved yet.")
            return
        if key in data_dict:
            clipboard.copy(data_dict[key])
            print("Copied the following data to the clipboard:")
            print(data_dict[key])
        else:
            print("No data saved with that key.")
def list_data():
    with open(data_file, 'r+') as f:
        try:
            data_dict = json.load(f)
        except ValueError:
            print("No data saved yet.")
            return
        print("Saved data:")
        for key, value in data_dict.items():
            print(f"{key}: {value}")
def main():
    if not os.path.exists(data_file):
        open(data_file, 'w').close()
    if len(sys.argv) < 2:
        print("Please provide a command: save, load, list.")
        return
    command = sys.argv[1]
    if command == 'save':
        if len(sys.argv) < 3:
            print("Please provide a key.")
            return
        key = sys.argv[2]
        data = clipboard.paste()
        save(key, data)
        print("Saved the following data under the key:")
        print(data)
    elif command == 'load':
        if len(sys.argv) < 3:
            print("Please provide a key.")
            return
        key = sys.argv[2]
        load(key)
    elif command == 'list':
        list_data()
    else:
        print("Unknown command. Please use: save, load, list.")
main() 
if __name__ == "__main__":
    main()
