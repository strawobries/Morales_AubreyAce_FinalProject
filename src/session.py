"""
Session Module

This module defines the Session class
for storing study session information.
"""


class Session:
    def __init__(
        self,
        session_id,
        subject,
        hours,
        minutes,
        seconds,
        date,
        notes
    ):
        self.session_id = session_id
        self.subject = subject
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.date = date
        self.notes = notes

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "subject": self.subject,
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
            "date": self.date,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data):
        return Session(
            data["session_id"],
            data["subject"],
            data["hours"],
            data["minutes"],
            data["seconds"],
            data["date"],
            data["notes"]
        )
