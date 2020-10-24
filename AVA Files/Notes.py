import datetime
import os
import subprocess
import AssistantSpeak as ASpeak
import CommandInput as CInput

# Function to instantly take down notes
def instantnote(text):
    date = datetime.datetime.now().date()
    save_path = "C:\\Users\\dell\\Documents\\GitHub\\AVA\\AVA\\AVA Files\\notes\\"
    ASpeak.speak("What do you want to name the file ?")
    file_name_input = CInput.get_command()
    file_name = save_path + file_name_input +" " + str(date).replace(":", "-") + "-note.txt"
    complete_name = os.path.join(save_path, file_name)
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
