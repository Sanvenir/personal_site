import os

from flask_script import Manager, Shell

from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context()))


@manager.command
def test():
    """
    Run the unit tests
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()
