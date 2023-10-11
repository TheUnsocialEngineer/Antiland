:orphan:

.. currentmodule:: discord

.. _intro:

Introduction
==============

This is the documentation for antiland.py, a python library that allows users to create bots On
and interactive with the Antiland.com platform

Prerequisites
---------------

This library works with Python 3.11 or higher. Support for earlier versions of Python
is not provided


.. _installing:

Installing
-----------

You can get the library directly from PyPI: ::

    pip3 install antiland

If you are upgrading versions then use the command below instead: ::

    py -3 -m pip install -U discord.py




Basic Concepts
---------------

Antiland.py revolves around the fact the antiland Platform uses pubnub as its messaging system which allows users
to access the data from chats which can then be used to detect specific events such as sending messages.

An example to showcase how this works:

.. code-block:: python3

   #coming soon
