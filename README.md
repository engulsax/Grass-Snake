# Grass-Snake
A python script which will notify you via email if a user snoops around in a pre-decided folder.
You have the option to take a webcam picture and attach it the email.

<b>Currently, this only works with gmail</b>

# How to use:
<ol>
	<li> Download the files on to your computer, you can do this in two ways: </li>
	<ul>
		<li>Either, download the grasssnaker_py folder to get a quick overview of the code </li>
		<li>Or, download the grasssnaker_exe folder which includes all the dependencies (choose this if you want to use the script)</li>
	</ul>
	<li> Open the info.txt and change the information in it to to set up the script </li>
	<li> If you get an SMTP Authentication Error (which you probably will get): </li>
	<ul>
		<li>You will need to allow less secure apps to access the sender email (the from email)</li>
		<li>This is how you do it: <a href="https://support.google.com/accounts/answer/6010255">Allow less secure apps to access your account</a></li>
	</ul>
	<li>Try again, and it should work.</li>
</ol>

<b>I do not recommend to turn on access to less secure apps on your main email address, instead create a secondary email address to send the emails</b>

# Info.txt
You can modify the following things:

foldername => The name of the map which should be covered by the script (type only the name, NOT the path!).

from email => The sender email.

to email => The reciver email.

email password = The password to the sender email.

Hours to live => The amount of time the script will be run.

Terminate if catched => If set to True the script will terminate after it sends the email.

Seconds between searches => The time in seconds between each search. Higher value = less realible

Use camera => If set to True, the script will use the device's webcam to snap an image and attatch it to the email.

Picture name => name of the attached image.

Message => Message which will be displayed in the email.

<b>Not that you can NOT have line breakes in a value in the info.txt files</b>

# Why the name "Grass Snake"?
Glad you asked! 

In Swedish Grass Snake = Snok.
If one were to transalate "snoka" from swedish to english it would be "snooping".

Also, grass snake was written in python, which makes the name fitting.

