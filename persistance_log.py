from pathlib import Path

data_file= Path("database.txt")
def daily_blocker():
    answer= input("\nWrite your daily blocker: ")
    return answer
if data_file.exists():
    print("----- WARNING -----\nThis file exists, the data that you will type is going to be appended not overwritten.")
else:   
    with open("database.txt", 'w') as file:
        file.write("DAILY BLOCKER:\n")

with open("database.txt", 'a', encoding= "utf-8") as file:
    file.write(f"DAILY BLOCKER: {daily_blocker()}\n")
def read_feature():
    try: 
        read_file = int(input("\nDo you want to watch the file?\n1.Yes\n2.No \nSelect a number : "))
        match read_file:
            case 1:
                if data_file.exists():
                    with open ("database.txt", 'r',encoding= "utf-8") as file:
                        for line in file:
                            print (line.strip())
                else:
                    print("***This file does not exist, nothing to read***")
                return read_file
            case 2:
                print("\nYour information was saved")
                return read_file
            case _:
                print("\nIncorrect choise")
                read_feature()
    except ValueError:
        print("\nYou had to insert a number")
        read_feature()
    
read_feature()
# --- Protocol Selection (3-C Rule: Clear, Concise, Courteous) ---
# I will reach out to the team via Slack because the issue is an immediate blocker
# that affects the file writing process and needs a fast response.
# If the bug requires tracking and history, I would report it through Jira
# so the team can assign priority and follow up properly.
# For a detailed explanation of the error, I would use Email to describe
# the problem clearly and attach the relevant file for review.

# --- Vocabulary Integration ---
# This script uses persistence to save the user's Daily Blocker to a .txt file,
# ensuring data is not lost between sessions. Before writing, it checks whether
# the file already exists to avoid an accidental overwrite, warning the user if
# needed. A fetch feature allows the user to read and display all stored entries
# directly in the Terminal. If any issue is found in this process, I will
# reach out to the team immediately through the appropriate communication channel.