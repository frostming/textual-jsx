import pyjsx.auto_setup  # noqa: F401
from counter import CounterApp

if __name__ == "__main__":
    application = CounterApp()
    application.run()
