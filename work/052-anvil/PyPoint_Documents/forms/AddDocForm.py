from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import utils

class AddDocForm(AddDocFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_errors.visible = False
    
    categories = anvil.server.call('get_all_categories')
    self.drop_down_category.items = (
      [("Select a category", None)] 
      + [(c["name"], c["name"]) for c in categories]
    )
    
    
  def validate_form(self):
    errors = []
    
    # Check title not empty
    if not self.text_box_title.text or not self.text_box_title.text.strip():
      errors.append("Title needs to be defined.")
      
    # Check category selected
    if not self.drop_down_category.selected_value:
      errors.append("Category needs to be selected.")
    
    # Check content not empty
    if not self.text_area_content.text:
      errors.append("Content can not be empty.")
      
    return errors

  
  def button_create_doc_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # Validated the form
    self.label_errors.visible = False
    errors = self.validate_form()
    if errors:
      self.label_errors.text = "\n".join(errors)
      self.label_errors.visible = True
    else:
      # TODO: Create the document in the database 
      anvil.server.call(
        'create_document', 
        title=self.text_box_title.text,
        category_name=self.drop_down_category.selected_value,
        content=self.text_area_content.text,
      )
      
      # "Redirect" to the home page
      utils.home_form_instance.go_home()