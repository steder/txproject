# txProject
## About

txProject is a set of utilities for quickly creating getting simple Twisted Python based
projects off the ground with all the convenient boilerplate already in place.

By providing a working skeleton with tests, plugin files, and basic configuration
txProject makes it easier for a twisted newbie to see how things fit together.  They
get an idea how they might organize their code and they have something that is working
immediately that they can begin to explore.

txProject is driven by basic templates and these templates can easily be customized
to provide more or fewer features to fit the developers needs.

## Installation

### Standard installation with Distutils

$ tar -zxvf txProject-1.0.tar.gz
$ cd txProject
$ python setup.py build
$ sudo python setup.py install

## Example Usage

txProject provides a txproject command.

### Creating a simple Twisted Web application

    $ txproject hello

This command creates the following:

    Hello/
    |-- bin/
    |-- hello/
    |   |-- test/
    |   |   `-- test_web.py
    |   `-- web.py
    `-- twisted/
            plugins/
                hello_plugin.py
                    
