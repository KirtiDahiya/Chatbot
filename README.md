# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###
BankHelpDesk
Project Documentation Installation:

Cloning Project:
git clone https://saty123@bitbucket.org/saty123/chatbotdm.git

If Necessary Installing libraries: pip install requirements.txt
Or you can activate the Environment.
Python Version=Python3



Project start:
Changing to Project Directory(in Terminal)
cd chatbotdm

Loading Environment
source env/bin/activate
	

Rabbitmq server:

	Installing Rabbit mq: Refer to the link
https://www.rabbitmq.com/install-debian.html

	Starting Rabbit mq Server

invoke-rc.d rabbitmq-server start(starting server)
invoke-rc.d rabbitmq-server stop(stopping server)

Checking status
sudo rabbitmqctl status

Note:start server before starting the project.

NiFi Server

How-to-install-and-start-nifi:
	Refer to the link:
	Note:Read the requirements carefully.(Java is necessary for running Nifi)

https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html#how-to-install-and-start-nifi

Server on another terminal

Home directory to where nifi is installed.

Change dir:cd nifi-1.2.0	
starting Nifi Server:bin/nifi.sh start

After Starting Nifi Server:
Upload Template from folder Nifi-Template.

(Check configurations)
Change mail id for receiving mail(Present:Singhal1153@gmail.com)
Mail Id for receiving Mail(Present:Bankhelpdesk17@gmail.com Password:satyamjaiswal)
SMTP server assigned to Gmail.(Can change provider)

 

Running Django Server:

cd bankhelpdesk
python manage.py runserver

		Note:Add  \chat to web adress to view the chatbot.



### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact