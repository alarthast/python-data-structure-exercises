# This program knows about the schedule for a conference that runs over the
# course of a day, with sessions in different tracks in different rooms.  Given
# a room and a time, it can tell you which session starts at that time.
#
# Usage:
#
# $ python conference_schedule.py [room] [time]
#
# For instance:
#
# $ python conference_schedule.py "Main Hall" 13:30
#
import sys

SCHEDULE = {
    "Main Hall": {
        "10:00": "Django REST framework",
        "11:00": "Lessons learned from PHP",
        "12:00": "Tech interviews that don't suck",
        "14:00": "Taking control of your Bluetooth devices",
        "15:00": "Fast Python? Don't Bother!",
        "16:00": "Test-Driven Data Analysis",
    },
    "Seminar Room": {
        "10:00": "Python in my Science Classroom",
        "11:00": "My journey from wxPython tp PyQt",
        "12:00": "Easy solutions to hard problems",
        "14:00": "Taking control of your Bluetooth devices",
        "15:00": "Euler's Key to Cryptography",
        "16:00": "Build your Microservices with ZeroMQ",
    },
    "Assembly Hall": {
        "10:00": "Distributed systems from scratch",
        "11:00": "Python in Medicine: ventilator data",
        "12:00": "Neurodiversity in Technology",
        "14:00": "Chat bots: What is AI?",
        "15:00": "Pygame Zero",
        "16:00": "The state of PyPy",
    },
}

SESSION_NAME_TO_ROOM_AND_TIME = {}
for room, room_schedule in SCHEDULE.items():
    for time, session in room_schedule.items():
        SESSION_NAME_TO_ROOM_AND_TIME[session] = (room, time)


NOT_FOUND = object()
CONFERENCE_END = "18:00"  # assumed


def _convert_to_minutes_since_midnight(time):
    """Convert a time in the HH:MM format to the number of seconds since the day began."""
    try:
        hh, mm = time.split(":")
        return hh * 60 + mm
    except ValueError:
        raise ValueError("Time must be provided in HH:MM format.")


def get_session(room, time):
    time_in_mins = _convert_to_minutes_since_midnight(time)

    try:
        room_schedule = SCHEDULE[room]
    except KeyError:
        return NOT_FOUND

    time_in_mins_to_session = {
        _convert_to_minutes_since_midnight(key): value
        for key, value in room_schedule.items()
    }

    session_times_in_mins = sorted(time_in_mins_to_session.keys())

    if time_in_mins < session_times_in_mins[0]:  # Before the first session starts
        return NOT_FOUND
    elif time_in_mins > _convert_to_minutes_since_midnight(CONFERENCE_END):
        return NOT_FOUND
    else:
        for session_time_in_mins in session_times_in_mins[::-1]:
            if time_in_mins >= session_time_in_mins:
                return time_in_mins_to_session[session_time_in_mins]
    assert False, f"Unable to determine slot for {time_in_mins}."


def main(args):
    if len(args) == 1:
        (session,) = args
        room, time = SESSION_NAME_TO_ROOM_AND_TIME.get(session, (NOT_FOUND, NOT_FOUND))
        if (room, time) == (NOT_FOUND, NOT_FOUND):
            message = f"Session {session} is not found."
        else:
            message = f"{session} is in the {room} at {time}."
    elif len(args) == 2:
        room, time = args
        session = get_session(room, time)
        if session is NOT_FOUND:
            message = f"There is not a session in {room} running at {time}."
        else:
            message = f"The session that is running in {room} at {time} is {session}."
    else:
        message = (
            "Input is invalid. Enter either a session name or a room/time combination."
        )
    print(message)


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that that it can tell you what session is running in
#   a room at a given time, even if a session doesn't start at that time.
# * Change the program so that if called with a single argument, the title of a
#   session, it displays the room and the time of the session.

if __name__ == "__main__":
    main(sys.argv[1:])
