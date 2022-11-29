"""
Mute 6 Audio Tracks

URL:

    http://github.com/khanrahan/mute-6-audio-tracks

Description:

    Toggles audio tracks 1-6 between mute or not on the selected sequences.

Menus:

    Right-click selected clips and/or sequences on the Desktop Reels --> Mute...
    --> Toggle Audio Tracks 1-6

    Right-click selected clips and/or sequences in the Media Panel --> Mute...
    --> Toggle Audio Tracks 1-6

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
"""

from __future__ import print_function

__title__ = "Mute 6 Audio Tracks"
__version_info__ = (0, 1, 1)
__version__ = ".".join([str(num) for num in __version_info__])
__title_version__ = "{} v{}".format(__title__, __version__)

MESSAGE_PREFIX = "[PYTHON HOOK]"


def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""

    print(" ".join([MESSAGE_PREFIX, string]))


def mute_6_tracks(selection):

    message(__title_version__)
    message("Script called from {}".format(__file__))

    for sequence in selection:
        for x in range(6):
            try:
                mute_status = sequence.audio_tracks[x].mute
                if mute_status == False:
                    sequence.audio_tracks[x].mute = True
                    continue
                if mute_status == True:
                    sequence.audio_tracks[x].mute = False
            except IndexError:
                pass

    message("Done!")


def scope_clip(selection):

    import flame

    for item in selection:
        if isinstance(item, flame.PySequence):
            return True
    return False


def get_media_panel_custom_ui_actions():

    return [{'name': "Mute...",
             'actions': [{'name': "Toggle Audio Tracks 1-6",
                          'isVisible': scope_clip,
                          'execute': mute_6_tracks,
                          'minimumVersion': "2020.3.1"}]
            }]
