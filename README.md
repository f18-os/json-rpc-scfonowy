# CS4375 - JSON RPC Lab
--
*by super anonymous student, last update November 12th, 2018*
## Overview
This lab implements a simple server/client RPC exercise supported by JSON RPC. The provided lab implements a Graph object as a container of Node objects. Node objects can have child Node objects. Note that there are several constraints on the graph:

* Every graph in the node must have a unique identifier (i.e. name).
* Every graph must have a node named "root" before being serialized for transmission.
* The graph may not contain cycles (note that this is not checked, but this will break the implementation).

The provided client code creates a small graph and, using the server, walks the graph, incrementing each node it encounters by 1. The server works off of a copy of the graph, so it's necessary for the client to update references as necessary.

A copy of the original assignment prompt is in ASSIGNMENT.md.

## Running Instructions
To run the lab, simply download or clone the repository and run the server script using `python3`. For example:

`python3 lab/server.py` or `./lab/server.py`

Then, start any number of clients in a similar fashion:

`python3 lab/client.py` or `./lab/server.py`

## References
Much of the code for setting up the RPC server and client was provided by Dr. Freudenthal.

Some examples and documentation were consulted for JSON serialization/deserialization. (https://gist.github.com/simonw/7000493, https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects, https://docs.python.org/3/library/json.html)

I also consulted this resource on Python library management. (http://www.owsiak.org/i-hate-python-importing-modules-from-subdirectories/)

