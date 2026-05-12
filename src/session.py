"""
Session Module

This module defines the Session class
for storing study session information.
"""


class Session:
    """
    Represents a study session record.
    """

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
        """
        Initializes a Session object.

        Args:
            session_id: Unique session ID.
            subject: Study subject name.
            hours: Study hours.
            minutes: Study minutes.
            seconds: Study seconds.
            date: Session date.
            notes: Additional notes.
        """

        self.session_id = session_id
        self.subject = subject
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.date = date
        self.notes = notes

    def to_dict(self):
        """
        Converts the session object into a dictionary.

        Returns:
            dict: Session data dictionary.
        """

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
        """
        Creates a Session object from dictionary data.

        Args:
            data: Dictionary containing session data.

        Returns:
            Session: New Session object.
        """

        return Session(
            data["session_id"],
            data["subject"],
            data["hours"],
            data["minutes"],
            data["seconds"],
            data["date"],
            data["notes"]
        )
