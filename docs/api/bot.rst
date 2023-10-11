Bot Class
=========

.. automodule:: antiland.bot
   :members:
   :undoc-members:
   :show-inheritance:

Introduction
------------

The `Bot` class is a part of the Antiland package, designed to work with Antiland accounts. It allows you to create and manage bots, perform various actions, and interact with Antiland's services.

Initialization
--------------

To create a `Bot` instance, you need to provide your authentication token.

.. code-block:: python

   from antiland.bot import Bot

   # Replace 'your_token' with your actual authentication token.
   bot = Bot('your_token')

Methods
-------

The `Bot` class provides the following methods:

- `login()`: Log in to an Antiland account using the provided token.
- `get_profile()`: Retrieve the profile information of the logged-in account.
- `update_profile()`: Update the profile information of the logged-in account.
- `get_bots()`: Get a list of bots associated with the logged-in account.
- `create_bot()`: Create a new bot associated with the logged-in account.
- `delete_bot()`: Delete a bot associated with the logged-in account.
- `get_dialogues()`: Retrieve a list of dialogues associated with the logged-in account.
- `get_messages()`: Get messages from a specific dialogue.
- `send_message()`: Send a message to a specific dialogue.
- `get_users()`: Get a list of users associated with the logged-in account.

These methods allow you to perform various actions related to Antiland accounts and interact with the platform's services.

Example
-------

Here's an example of how to use the `Bot` class:

```python
from antiland.bot import Bot

# Replace 'your_token' with your actual authentication token.
bot = Bot('your_token')

# Log in to the account.
bot.login()

# Get the profile information.
profile_info = bot.get_profile()
print(profile_info)
