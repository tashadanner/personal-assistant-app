class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {
      'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer', 'Neal': "Website Designer", 'Rachel': 'Admin Asst'
      }
    self.todos = todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name."

  def add_todo(self, new_item):
      self.todos.append(new_item)

  def remove_todo(self, todo_item):
      if todo_item in self.todos:
    # Get the todo_item index in list
        index = self.todos.index(todo_item)
    # pop the index for todo_item in todos list
        self.todos.pop(index)
      else:
        print("To-do is not in list!")

  def get_todo(self):
      return self.todos

  def get_birthday(self,name):
      if name == "Neal":
        return "Birthday is 3/8/1970"
      elif name== "Kathy":
        return "Birthday is 10/14/1949"
      elif name == "Tom":
        return "Birthday is 11/4/1948"
      elif name == "Jon":
        return "Birthday is 12/29/1948"
      elif name == "Toby":
        return "Birthday is 4/17/1969"
      else:
        return "Can't find a birthday for this person"
    

# Code to test output of the class
#assistant = PersonalAssistant()
#assistant.add_todo("Pick up cat food")
#assistant.add_todo("Write to lawyers")
#print(assistant.get_todo())
#assistant.remove_todo ("Pick up cat food")
# Change name to one from your contacts
#print(assistant.get_contact("Rachel"))
#print(assistant.get_birthday("Neal"))