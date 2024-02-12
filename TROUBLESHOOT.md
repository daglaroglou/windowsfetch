 # Contents
 
 - [Taking too long to run](https://github.com/daglaroglou/windowsfetch/blob/main/TROUBLESHOOT.md#taking-too-long-to-run)
 - [xxxx module not found](https://github.com/daglaroglou/windowsfetch/blob/main/TROUBLESHOOT.md#xxxx-module-not-found)
 - [Permission denied](https://github.com/daglaroglou/windowsfetch/blob/main/TROUBLESHOOT.md#permission-denied)
 - ["This program works only on Windows OS!"](https://github.com/daglaroglou/windowsfetch/blob/main/TROUBLESHOOT.md#taking-too-long-to-run)


# Taking too long to run

1. Close the current program
2. Launch a new Command Prompt
3. Type `winget list` and hit `y` on the aggreements page
4. Re-launch windowsfetch.py

# xxxx module not found

Make sure that you have all the libraries installed.

If you cant find which is missing run: `pip install -r requirements.txt`.

# Permission denied

1. Right click on `windowsfetch.py`
2. Click properties
3. Go on `Security` tab
4. Click "Edit"
5. Give all permissions
6. Re-launch windowsfetch.py

# "This program works only on Windows OS!"

Your are most probably trying to run windowsfetch on a Linux machine.

Be aware that it **only** works on **Windows OS**.
