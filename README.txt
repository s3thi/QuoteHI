
QuoteHI is a Pylons application for collecting IRC quotes. I wrote
this to experiment with writing webapps in Python.

Installation and Setup
======================


  Step 1: Install Pylons and its dependencies:

    $ sudo easy_install pylons

  I've tested the application with Pylons 1.0 on Linux and OS X.
  
  
  Step 2: Install MongoDB. Linux users can find the instructions on
  MongoDB.org. OS X users with MacPorts can do:

    $ sudo port install mongodb

  
  Step 3: Install PyMongo:

    $ sudo easy_install pymongo

  Alternatively, download and install it from the archive on MongoDB.org.

  
  Step 4: Run MongoDB:

    $ mongod --dbpath=/path/to/data/directory/


  Step 5: Run QuoteHI:

    $ paster serve development.ini

  You should now be able to access it from http://127.0.0.1:5000.


  Tested and confirmed working inside a virtualenv.
