import datetime

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#

@anvil.server.callable
def create_document(title, category_name, content):
  now = datetime.datetime.now()
  category = get_category_by_name(name=category_name)
  app_tables.documents.add_row(
    title=title,
    category=category,
    content=content,
    created=now,
  )

  
@anvil.server.callable  
def get_all_documents():
  return list(
    app_tables.documents.search(
      tables.order_by("created", ascending=False),
    )
  )


@anvil.server.callable  
def get_recent_documents():
  return list(
    app_tables.documents.search(
      tables.order_by("created", ascending=False),
    )[:3]
  )
  
  
@anvil.server.callable  
def get_all_categories():
  return list(app_tables.categories.search())


def get_category_by_name(name):
  return app_tables.categories.get(name=name)