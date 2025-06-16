# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicLibrary:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        self.music_library = []

    def add(self, track):
        """
        adds a track to the music library list.
        """
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def list_tracks(self):
        """
        returns music library list
        """
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
User can create an empty music libray
returns an empty list
"""

"""
If User tries to list tracks without any being added
Returns an error
"""

"""
If user tries to add an empty string
returns an error
"""

"""
User is able to add one track
List_tracks will return this track
"""

"""
User is able to add multiple tracks
List_tracks will return the same multiple tracks
"""

