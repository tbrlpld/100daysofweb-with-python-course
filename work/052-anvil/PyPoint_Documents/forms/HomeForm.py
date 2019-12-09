from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import utils

from .HomeContentForm import HomeContentForm
from .AllDocsForm import AllDocsForm
from .AddDocForm import AddDocForm
from .DocDetailForm import DocDetailForm

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    utils.home_form_instance = self
    
    self.go_home()

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_home()
  
  def link_all_docs_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(AllDocsForm())

  def link_add_doc_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(AddDocForm())
    
  def go_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(HomeContentForm())

  def show_doc_detail(self, doc):
    self.content_panel.clear()
    self.content_panel.add_component(DocDetailForm(item=doc))
