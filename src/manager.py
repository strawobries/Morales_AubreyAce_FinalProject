"""
Session Manager Module

This module handles all study session
management functions in the application.
"""

import json
import os
from session import Session


class SessionManager:
    """
    Manages all study session operations.
    """

    def __init__(self):
        """
        Initializes the SessionManager object.
        """

        self.sessions = []

        self.file_path = os.path.join(
            "data",
            "sessions.json"
        )

    def add_session(self, session):
        """
        Adds a new study session.

        Args:
            session: Session object to add.
        """

        if any(
            s.session_id == session.session_id
            for s in self.sessions
        ):
            print("Session ID already exists.")
            return

        self.sessions.append(session)

        print("Session added successfully.")

    def view_sessions(self):
        """
        Displays all study sessions.
        """

        if not self.sessions:
            print("No sessions found.")
            return

        print("\n--- Study Sessions ---")

        for s in self.sessions:
            print(f"ID: {s.session_id}")
            print(f"Subject: {s.subject}")

            print(
                f"Duration: "
                f"{s.hours}h "
                f"{s.minutes}m "
                f"{s.seconds}s"
            )

            print(f"Date: {s.date}")
            print(f"Notes: {s.notes}")

            print("-" * 30)

    def search_session(self, session_id):
        """
        Searches for a study session.

        Args:
            session_id: ID of the session.
        """

        for s in self.sessions:
            if s.session_id == session_id:

                print("\n--- Session Found ---")

                print(f"ID: {s.session_id}")
                print(f"Subject: {s.subject}")

                print(
                    f"Duration: "
                    f"{s.hours}h "
                    f"{s.minutes}m "
                    f"{s.seconds}s"
                )

                print(f"Date: {s.date}")
                print(f"Notes: {s.notes}")

                return

        print("Session not found.")

    def delete_session(self, session_id):
        """
        Deletes a study session.

        Args:
            session_id: ID of the session.
        """

        for s in self.sessions:
            if s.session_id == session_id:

                self.sessions.remove(s)

                print(
                    "Session deleted successfully."
                )

                return

        print("Session not found.")

    def update_session(self, session_id):
        """
        Updates an existing study session.

        Args:
            session_id: ID of the session.
        """

        for s in self.sessions:
            if s.session_id == session_id:

                print(
                    "Leave blank to keep "
                    "current value."
                )

                subject = input(
                    f"New subject "
                    f"({s.subject}): "
                )

                duration = input(
                    f"New duration "
                    f"({s.hours:02}:"
                    f"{s.minutes:02}:"
                    f"{s.seconds:02}): "
                )

                date = input(
                    f"New date "
                    f"({s.date}) "
                    f"(MM-DD-YYYY): "
                )

                notes = input(
                    f"New notes "
                    f"({s.notes}): "
                )

                if subject:
                    s.subject = subject

                try:
                    if duration:

                        (
                            s.hours,
                            s.minutes,
                            s.seconds

                        ) = map(
                            int,
                            duration.split(":")
                        )

                except ValueError:
                    print("Invalid duration format.")

                if date:
                    s.date = date

                if notes:
                    s.notes = notes

                print(
                    "Session updated successfully."
                )

                return

        print("Session not found.")

    def sort_sessions(self):
        """
        Sorts study sessions alphabetically.
        """

        self.sessions.sort(
            key=lambda s: s.subject.lower()
        )

        print("\n--- Sorted Sessions ---")

        for s in self.sessions:
            print(f"ID: {s.session_id}")
            print(f"Subject: {s.subject}")

            print(
                f"Duration: "
                f"{s.hours}h "
                f"{s.minutes}m "
                f"{s.seconds}s"
            )

            print(f"Date: {s.date}")
            print(f"Notes: {s.notes}")

            print("-" * 30)

    def count_sessions(self):
        """
        Displays total number of sessions.
        """

        print(
            f"Total sessions: "
            f"{len(self.sessions)}"
        )

    def total_study_time(self):
        """
        Calculates total study time.
        """

        total_seconds = sum(
            (s.hours * 3600) +
            (s.minutes * 60) +
            s.seconds
            for s in self.sessions
        )

        hours = total_seconds // 3600

        minutes = (
            total_seconds % 3600
        ) // 60

        seconds = total_seconds % 60

        print(
            f"Total study time: "
            f"{hours}h "
            f"{minutes}m "
            f"{seconds}s"
        )

    def save_to_file(self):
        """
        Saves session data into a JSON file.
        """

        os.makedirs("data", exist_ok=True)

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                [
                    s.to_dict()
                    for s in self.sessions
                ],
                file,
                indent=4
            )

        print("Data saved successfully.")

    def load_from_file(self):
        """
        Loads session data from a JSON file.
        """

        if not os.path.exists(self.file_path):
            print("No saved file found.")
            return

        with open(
            self.file_path,
            "r"
        ) as file:

            data = json.load(file)

        self.sessions = [
            Session.from_dict(item)
            for item in data
        ]

        print("Data loaded successfully.")
