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


NOT_FOUND = ""


def floor_to_nearest_hour(time):
    """Convert a time in the HH:MM format to HH:00 format."""
    try:
        hh, mm = time.split(":")
        num_mins_since_midnight = int(hh) * 60 + int(mm)
    except ValueError:
        raise ValueError("Time must be provided in HH:MM format.")
    return num_mins_since_midnight // 60


def get_session(room, time):
    nearest_hour = floor_to_nearest_hour(time)
    session_start_time = f"{nearest_hour}:00"
    session = SCHEDULE.get(room, {}).get(session_start_time, NOT_FOUND)
    return session


def get_room_and_time(session):
    return SESSION_NAME_TO_ROOM_AND_TIME.get(session, ("", ""))


def parse_args(args):
    try:
        _, session = args
        return (session, "", "")
    except ValueError:
        try:
            _, room, time = args
            return ("", room, time)
        except ValueError:
            return ("", "", "")


def main(args):
    session, room, time = parse_args(args)
    if session:
        room, time = get_room_and_time(session)
        if room and time:
            message = f"{session} is in the {room} at {time}."
        else:
            message = f"Session {session} is not found."
    elif room and time:
        session = get_session(room, time)
        if session:
            message = f"The session that is running in {room} at {time} is {session}."
        else:
            message = f"There is not a session in {room} running at {time}."
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
    main(sys.argv)
