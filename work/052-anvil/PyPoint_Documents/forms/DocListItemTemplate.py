from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import utils

class DocListItemTemplate(DocListItemTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_created.text = self.item["created"].strftime("%B %d, %Y")

  def link_detail_click(self, **event_args):
    """This method is called when the link is clicked"""
    utils.home_form_instance.show_doc_detail(self.item)

