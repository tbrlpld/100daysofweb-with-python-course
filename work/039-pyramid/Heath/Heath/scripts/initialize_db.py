import argparse
import datetime
import json
import os
import sys

from pyramid.paster import bootstrap, setup_logging, get_appsettings
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    users = get_users()
    dbsession.add_all(users)

def get_users():
    """Return list of user objects."""
    user_dicts = load_user_data()
    user_objs = []
    for user in user_dicts:
        user_objs.append(models.user.User(
            name=user["name"],
            email=user["email"],
            password=user["password"],
            created=datetime.datetime.strptime(
                user["created"],
                "%Y-%m-%dT%H:%M:%SZ",
            ),
        ))
    return user_objs


def load_user_data():
    """Parse mock User data into dict."""
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    user_json_path = os.path.join(parent_dir, "db", "Users.json")
    with open(user_json_path, "r") as user_file:
        user_dict = json.load(user_file)
    return user_dict



def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
