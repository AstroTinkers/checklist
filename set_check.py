import datetime as datetime
check_set = set()
while True:
    input_data = input("Input(Press q to exit):")
    if input_data == "q":
        if len(check_set) == 0:
            break
        else:
            final_list = sorted(check_set, key=lambda idc: (idc.isnumeric(), int(idc) if idc.isnumeric() else idc))
            # idc - input data check - checks every entry if it's integer or strings and sorts accordingly
            file_name = input("Please enter name for your checklist:") or "Checklist"
            timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
            file_name = f"{file_name}_{timestamp}.txt"  # adds name and timestamp
            textfile = open(file_name, "x")
            for elements in final_list:
                textfile.write(elements + "\n")
            textfile.close()
            print(final_list)
        break
    elif input_data == "":
        continue
    elif input_data in check_set:
        print("You already got one.")
    else:
        check_set.add(input_data)
        print("Item added to checklist.")
