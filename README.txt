About
=====

QuoteHI is a quotes collector built using Pylons and MongoDB. Besides
PyMongo -- the Python driver for MongoDB -- QuoteHI uses MongoKit for type
checking and validation.


Installation and Setup
======================

  Step 1: Install Pylons and its dependencies:

    $ sudo easy_install pylons

  I've tested the application with Pylons 1.0 on Linux and OS X.
  
  
  Step 2: Install MongoDB. Linux users can find the instructions on
  MongoDB.org. OS X users with MacPorts can do:

    $ sudo port install mongodb

  Alternatively, download and install it from the archive on MongoDB.org.
  

  Step 3: Install PyMongo and MongoKit

    $ sudo easy_install pymongo mongokit

  You could also do what I do and use pip instead of easy_install.
  

  Step 4: Run MongoDB:

    $ mongod --dbpath=/path/to/data/directory/


  Step 5: Run setup-app to add an initial user:

    $ paster setup-app development.ini

  
  Step 6: Run QuoteHI:

    $ paster serve development.ini

  You should now be able to access it from http://127.0.0.1:5000.


  Warning: do not use the default configuration file (development.ini) in a
  production environment.
