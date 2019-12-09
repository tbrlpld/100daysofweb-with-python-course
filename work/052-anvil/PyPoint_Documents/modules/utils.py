import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This module defines some helpers that are used in mutiple places


# The home form instance saved it self to this variable. 
# This is to make the home form methods callable from other forms, 
# without creating cirular dependencies.
home_form_instance = None
