
import logging

from gui import SmartApp


def main():
    logging.basicConfig(level=logging.INFO)
    app = SmartApp()
    app.mainloop()


if __name__ == "__main__":
    main()