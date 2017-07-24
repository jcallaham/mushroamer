# Mushroamer
## Northeast *Lactarius* sieve

Version 0.1
July 24th, 2017

### Overview

The end goal of the project is a multi-platform mobile app that can be used
to aid in mushroom identification. An important feature of the project is that
it should be easy to add more mushroom families and data to the database.

The current state of the project is a simple text website written in Django and
hosted using Google's App Engine with a Cloud SQL database. 

**Next Steps**
- Nice-looking website formatting
- Use Firebase to develop mobile apps
- Nice-looking app formatting


### Project Structure

For now, the project contains two distinct Django apps, although these could (and maybe should)
be combined into one. I also used a **virtualenv** environment to develop the apps in Python 2.7

**Encyclopedia**
This is just an index of all species in the database, with links to detail pages. A nice improvement
would be to have images on the detail pages, loaded from an image directory

**Sieve**
This is the search functionality. It populates a form with all of the characters and possible selections
from the database and searches for percent match based on the user response. It is designed to ignore fields
that haven't been completed, so the user can hopefully find possible matches without making all of the possible
observations

I chose the percent match approach instead of a typical database filter so that the user can potentially make mistakes
in identification (e.g. "white" instead of "grey") and still find the correct match. An important consequence of this
is that this app shouldn't be considered a definitive answer when it comes to identification, especially when it
comes to edibility. The project was designed to be a tool to help experienced mushroamers.


### How to update the database
The database is currently generated from the .csv file in /data/lactarius-test.csv. To recreate the database, run
the shell script rebuild.sh, which calls the Python script build_database.py. The name of the csv file can be changed
in build_database.py

Note that for the current project you need permission to access the Cloud SQL database in order to do this.


### License

This project is licensed under the GNU GPL - see the LICENSE.md file for details


