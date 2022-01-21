import datetime as datetime
import os
check = set()
while True:
    input_data = input("Input(Press q to exit):")
    if input_data == "q":
        if len(check) == 0:
            break
        else:
            final = list(check)
            final.sort()
            file_name = input("Please enter name for your checklist:")
            file_name = file_name + " " + datetime.datetime.now().strftime("%d-%m-%Y - %H-%M") + ".txt" #adds name
            # and timestamp
            file_name = str(file_name)
            if os.path.isfile(file_name): #checks if file already exists and adds a number
                counter = 1
                while True:
                    counter += 1
                    new_file_name = file_name.split(".txt")[0] + "-" + str(counter) + ".txt"
                    if os.path.isfile(new_file_name):
                        continue
                    else:
                        file_name = new_file_name
                        break
            textfile = open(file_name, "x")
            for elements in final:
                textfile.write(elements + "\n")
            textfile.close()
            print(final)
        break
    elif input_data in check:
        print("You already got one.")
    else:
        check.add(input_data)
        print("Item added to checklist.")
