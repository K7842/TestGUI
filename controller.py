class Controller:
    # The init function just creates empty variables for the model and view.
    def __init__(self):
        self.model = None
        self.view = None

    # The configure function is called by main.py to pass in the model and view objects.
    def configure(self, model, view):
        self.model = model
        self.view = view

    def get_first_ticket(self):
        return self.model.all_tickets[0]

    def initial_setup(self):
        # Get all tickets.
        all_tickets = self.model.all_tickets
        # Refresh ticket section with all tickets.
        self.view.ticket_bar.refresh_ticket_section(all_tickets)

    def handle_ticket_clicked(self, event):
        # First need to save the currently open ticket.

        # Get the ticket name from the label.
        ticket_name = event.widget['text']
        # Get the ticket object from the model.
        self.model.get_ticket(ticket_name)
        # Open the ticket in the ticket detail section.
        # print(self.model.current_ticket[1])
        self.view.ticket_details.load_ticket(
            self.model.current_ticket[1], ticket_name)

    def handle_new_ticket_clicked(self):
        ticket = None
        self.view.ticket_details.load_ticket(ticket, "")

    def list_all_case_names(self):
        all_case_names = [case.manufacturer + ' ' +
                          case.SKU for case in self.model.all_cases]
        return all_case_names

    def select_case_clicked(self, event):
        all_case_names = self.list_all_case_names()

        # print(event.type)

        if event.type == '4':
            self.view.ticket_details.open_search_box(all_case_names)
        elif event.type == '2':
            self.view.ticket_details.select_item()
        elif event.type == '3':
            self.view.ticket_details.search_box_key_release()

    def delete_ticket(self, name):
        self.view.ticket_bar.ticket_frames.pop(name)

    def add_case():
        pass
