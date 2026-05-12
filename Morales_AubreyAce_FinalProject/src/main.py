"""
Main Module

This module runs the Study Time application.
"""

from session import Session
from manager import SessionManager


def menu():
    print("\n===== Study Time =====")
    print("1. Add Session")
    print("2. View Sessions")
    print("3. Search Session")
    print("4. Delete Session")
    print("5. Update Session")
    print("6. Sort Sessions")
    print("7. Count Sessions")
    print("8. Total Study Time")
    print("9. Save")
    print("10. Load")
    print("11. Exit")


def main():
    manager = SessionManager()

    while True:
        menu()

        choice = input(
            "Enter choice: "
        ).strip()

        if choice == "1":
            try:
                session_id = input(
                    "Enter ID: "
                ).strip()

                subject = input(
                    "Enter subject: "
                ).strip()

                duration = input(
                    "Enter duration "
                    "(HH:MM:SS): "
                ).strip()

                hours, minutes, seconds = map(
                    int,
                    duration.split(":")
                )

                date = input(
                    "Enter date "
                    "(MM-DD-YYYY): "
                ).strip()

                notes = input(
                    "Enter notes: "
                ).strip()

                if (
                    not session_id
                    or not subject
                ):
                    print(
                        "ID and Subject "
                        "are required."
                    )

                    continue

                new_session = Session(
                    session_id,
                    subject,
                    hours,
                    minutes,
                    seconds,
                    date,
                    notes
                )

                manager.add_session(
                    new_session
                )

            except ValueError:
                print(
                    "Invalid duration format. "
                    "Use HH:MM:SS"
                )

        elif choice == "2":
            manager.view_sessions()

        elif choice == "3":
            session_id = input(
                "Search ID: "
            ).strip()

            manager.search_session(
                session_id
            )

        elif choice == "4":
            session_id = input(
                "Enter ID to delete: "
            ).strip()

            manager.delete_session(
                session_id
            )

        elif choice == "5":
            session_id = input(
                "Enter ID to update: "
            ).strip()

            manager.update_session(
                session_id
            )

        elif choice == "6":
            manager.sort_sessions()

        elif choice == "7":
            manager.count_sessions()

        elif choice == "8":
            manager.total_study_time()

        elif choice == "9":
            manager.save_to_file()

        elif choice == "10":
            manager.load_from_file()

        elif choice == "11":
            print(
                "Well Done, Keep it up!"
            )

            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
