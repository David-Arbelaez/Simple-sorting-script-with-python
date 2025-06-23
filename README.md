# Simple-sorting-script-with-Python
Use this simple code to organize your files according to their extensions in different folders automatically. It is fully customizable, and can be programmed to run on system startup. Let's see what it's all about!

<br/>

<h1>Getting Started 👨‍🦯‍➡️</h1>
Make sure you have <b>Python 3.6</b> before proceeding with the instructions. You can download it directly from its <a href="https://www.python.org/downloads/release/python-360/">official website.<a/> <br/><br/>

In order to run the program we will use the <a href="https://python-watchdog.readthedocs.io/en/stable/">watchdog<a/> library, which detects real-time changes in files or folders, such as when they are created, modified or deleted, and allows to execute actions in response to those events. <br/><br/>
You can install the library directly from a terminal using the following command:<br/>

```
pip install watchdog
```

Download the file <b>Organizer.py</b> and open it with your favorite code editor. Since we will only make a few simple changes, you can use notepad. Select the folder you want to organize and copy the path. Look inside the code for the space to put your path and replace <i>C:\source\dir\path</i> with your own address.<br/><br/>
![image](https://github.com/user-attachments/assets/0f375630-9d70-486c-afb2-029b23f5f048)

The code is already programmed to organize your files in 4 categories: notes, images, scripts and documents. But you can customize it to your liking with the steps in the [personalization](#Personalization) section. Create the destination folders for each of the 4 categories, copy the paths and add the addresses in each of the code sections. <br/><br/>
![image](https://github.com/user-attachments/assets/08b6a930-1d6b-44d5-ab3d-8b00d90f2e1f)


<h2>Auto start up (Windows)🤖</h2>
The fun thing about the program is that it works constantly without having to activate it, even if you reboot your system. To activate this functionality just follow these simple steps:<br/><br/>
Copy the path to the <i>Organizer.py</i> file and save it in a notepad.<br/><br/>
We will also need the route of <i>pythonw.exe</i> so that the script is executed when the system is turned on. The easiest way to find it is to use this command in the terminal:<br/><br/>

```
where pythonw
```
copy the path and paste it into notepad. <br/><br/>
Open the "<b>Run</b>" window by pressing <b>CTRL+R</b> and there copy the following command:<br/>
```
shell:startup
```
This will open the folder of programs that start automatically with the system. Now we must create a new shortcut for our script. Right click, new, shortcut. A window will open with a text box where you paste both links from the notepad, and it should look something like this:

```
"C:\Users\MyUser\AppData\Local\Microsoft\WindowsApps\pythonw.exe" "C:\Users\MyUser\Downloads\Organizer.py"

```
click ok and restart your system. Congratulations, your folders are now automatically organized 🥳🎉.
<h2>Personalization</h2>

