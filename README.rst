====================
PMR Exposure Mockups
====================

In this repository we are exploring options for various ways that we might want to visualise and interact with the data contained in a (CellML) PMR workspace. All these mockups should be treated as prototypes and not definitive demonstrations of what future PMR exposures will look like.

Python webserver
================

Due to the requirements of Javascript and HTML development, it is nescessary to make use of a webserver to serve the HTML and JS files. For convenience, we include a simple wrapper script in the `server <server>`_ folder which makes use of the python 3 builtin http server.

The best way to run this is to simply go to *this* folder in your clone of the mockups repository and run ``python3 server/server.py`` in a terminal. (``python3`` is the name of the python 3 interpreter on my system, the name may vary on your system.)
