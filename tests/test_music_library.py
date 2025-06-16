from lib.music_library import *
import pytest

"""
User can create an empty music libray
returns an empty list
"""

def test_user_can_create_empty_music_library():
    library = MusicLibrary()
    assert library.music_library == []

"""
If User tries to list tracks without any being added
Returns an error
"""

def test_raises_error_when_user_calls_list_tracks_on_empty_library():
    library = MusicLibrary()
    with pytest.raises(Exception) as error:
        library.list_tracks()
    error_message = str(error.value)
    assert error_message == 'Error: Library currently empty'

"""
User is able to add one track
List_tracks will return this track
"""

def test_user_can_add_one_track():
    library = MusicLibrary()
    library.add('Song 1')
    result = library.list_tracks()
    assert result == ['Song 1']



"""
If user tries to add an empty string
returns an error
"""


"""
User is able to add multiple tracks
List_tracks will return the same multiple tracks
"""

