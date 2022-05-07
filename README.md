# Overview

I am trying to learn how to use Python for networking purposes. I am new to the Python language. I found out about the socket libraries in Python, and I decided I wanted to try writing a program that uses sockets to perform basic networking functions. I want to deepen my understanding of inter-computer communication and how it works, and I thought this would be a good project to start with.

I wrote a networking program that will send a message to another computer given the IP address. It sends three messages, and after each message it waits for input from the client side before it continues to the next message. It has a simple graphical user interface that facilitates the use of the application. Currently it needs to be run in an IDE, but there's a possibility of expanding it to the command line. The server file needs to be started and running on one computer, and the client file needs to be running on the other computer. When he client file runs, it sends the messages. There are messages in the files showing how far into the code you are, all the way up until you hit the part of the code that breaks the connection.

My purpose for writing this software was to learn the basics of networking and see how computers can communicate directly with each other. I know that networking is a large part of the internet, and it is the foundation of the world wide web. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}
I used the client/server model. I didn't have any particular reason for choosing that. I know that most communication on the web is client/server, so I wanted to understand that relationship more.

{Identify if you are using TCP or UDP and what port numbers are used.}

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

I used VS Code and the downloadable version of Python 3 for this project. VS Code has useful Python extensions that made this project a little easier.

I also found a Python library for simple graphical user interfaces called PySimpleGUI. Of course, I also used the socket library on Python for the basic networking functionality, as the library is extensive and useful for that sort of thing.

# Useful Websites

* [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/themes-in-pysimplegui/)

# Future Work

* The graphical user interface could use a more sophisticated and sleek look.
* The program could use some error checking features. It would do well to have something that checks that the user put the IP address in in the correct format.
* Item 3
