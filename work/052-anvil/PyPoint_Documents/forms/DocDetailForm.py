from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class DocDetailForm(DocDetailFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    doc = self.item
    self.display_category.text = doc["category"]["name"]
    self.display_created.text = doc["created"].strftime("%B %d, %Y")
    
    