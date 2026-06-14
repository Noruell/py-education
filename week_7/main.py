from Education.week_7.commands import main
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data", "state.json")

if __name__ == "__main__":
    main()