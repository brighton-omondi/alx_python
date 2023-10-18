import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_letter_a(username, password, database_name):
    try:
        # Define your MySQL connection URL
        db_url = f"mysql://{username}:{password}@localhost:3306/{database_name}"

        # Create an engine
        engine = create_engine(db_url, echo=False)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State objects with names containing the letter 'a'
        states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

        # Display the results
        for state in states:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()

    except Exception as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states_with_letter_a(username, password, database_name)
