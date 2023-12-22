import tkinter
import tkinter.ttk
import sqlite3

from model import Model


class View(tkinter.Tk):
    def __init__(self, controller):
        super().__init__()

        # Basic window setup.
        self.title('PC Building Simulator')
        self.minsize(800, 600)

        # Reference to controller object to be called for user interactions.
        self.controller = controller

        # Left Side - Ticket Bar
        # Right Side - Ticket Details
        self.ticket_bar = Container_Ticket_Bar(self, controller)
        self.ticket_details = Container_Ticket_Details(self, controller)

        self.ticket_bar.pack(side='left', fill='y')
        self.ticket_details.pack(side='left', fill='y')

        #### MENU ####

        self.menu = tkinter.Menu(self)
        self.config(menu=self.menu)

        # Create file manu and add cascade.
        file_menu = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)

        # Create modify menu and add cascade.
        modify_menu = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Modify", menu=modify_menu)

        # Set modify menu options.
        modify_menu.add_command(
            label="Add Case", command=self.controller.add_case)
        modify_menu.add_command(label="Add RAM")
        modify_menu.add_command(label="Add GPU")

        # Create help menu and add cascade.
        help_menu = tkinter.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)

        #### END MENU ####

    def run(self):
        self.controller.initial_setup()
        self.mainloop()

    def show_ticket_details(self):
        self.ticket_details.pack(side='left', fill='y')


class Container_Ticket_Bar(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, background='light grey', padx=10, pady=5)

        self.controller = controller

        self.all_ticket_frames = []

        newticket_button = tkinter.Button(
            self, text="New Ticket", width=10, command=self.controller.handle_new_ticket_clicked)
        newticket_button.pack(side='bottom', pady=10)

    def refresh_ticket_section(self, all_tickets):
        for i, ticket in enumerate(all_tickets):
            if i < 7:
                frame = tkinter.Frame(
                    self, width=75, height=75, borderwidth=1, relief="solid")
                frame.pack_propagate(False)
                l_name = tkinter.Label(frame, text=ticket.name)
                l_name.bind(
                    "<Button-1>", self.controller.handle_ticket_clicked)
                l_name.pack(expand=True, fill='both')
                frame.pack(side='top')
                self.all_ticket_frames.append(frame)


class Container_Ticket_Details(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.previous_ticket_owner = ''
        self.previous_ticket = None

        self.general_components = [
            ['Name', None, 'name', tkinter.StringVar()],
            ['Labour', None, 'labour', tkinter.StringVar()],
            ['Budget', None, 'budget', tkinter.StringVar()],
            ['Due', None, 'due', tkinter.StringVar()],
            ['New Parts', None, 'new_parts', tkinter.StringVar()],
            ['Manufacturer', None, 'manufacturer', tkinter.StringVar()],
            ['Dust', None, 'dust', tkinter.StringVar()],
            ['Virus', None, 'virus', tkinter.StringVar()],
            ['Cable Colour', None, 'cable_colour', tkinter.StringVar()],
            ['3DMark', None, 'D3Mark', tkinter.StringVar()],
            ['Will It Run', None, 'will_it_run', tkinter.StringVar()],
            ['Specification', None, 'spec', tkinter.StringVar()]
        ]
        self.computer_components = [
            ['CPU', None, None, None, 'CPU', tkinter.StringVar()],
            ['Cooling', None, None, None, 'Cooling', tkinter.StringVar()],
            ['Motherboard', None, None, None, 'Motherboard', tkinter.StringVar()],
            ['RAM', None, None, None, 'RAM', tkinter.StringVar()],
            ['GPU', None, None, None, 'GPU', tkinter.StringVar()],
            ['Storage', None, None, None, 'Storage', tkinter.StringVar()],
            ['PSU', None, None, None, 'PSU', tkinter.StringVar()],
            ['Case', None, None, None, 'PCCase', tkinter.StringVar()],
            ['Case Fans', None, None, None, 'Case_Fans', tkinter.StringVar()]
        ]

        # Loop through the general components and create labels, entries and bindings for them.
        for i, component in enumerate(self.general_components):

            # Create the widgets.
            label = tkinter.Label(self, text=component[0] + ":")
            entry = tkinter.Entry(self, textvariable=component[3])

            # Put them on the grid.
            label.grid(row=i, column=0, sticky="w")
            entry.grid(row=i, column=1)

            # Store the references to the widgets.
            component[1] = entry

            # Bind UP key to move up the entry list as long as it's not the first entry
            if i > 0:
                entry.bind("<Up>", lambda event,
                           i=i: self.general_components[i-1][1].focus_set())

            # Bind DOWN key to move down the entry list as long as it's not the last entry.
            if i < len(self.general_components) - 1:
                entry.bind("<Down>", lambda event,
                           i=i: self.general_components[i+1][1].focus_set())

        # Loop through the computer components and create labels, entries and bindings for them.
        for i, component in enumerate(self.computer_components):

            # Create the widgets.
            label = tkinter.Label(self, text=component[0] + ":")
            entry = tkinter.Entry(self, textvariable=component[5])
            checkbutton = tkinter.Checkbutton(self, text="Replace")
            replace_entry = tkinter.Entry(self)

            # Put them on the grid.
            label.grid(row=i, column=2, sticky="w")
            entry.grid(row=i, column=3)
            checkbutton.grid(row=i, column=4)
            replace_entry.grid(row=i, column=5)

            # Store the references to the widgets.
            component[1:4] = entry, checkbutton, replace_entry

            # Bind UP key to move up the entry list as long as it's not the first entry
            if i > 0:
                entry.bind("<Up>", lambda event,
                           i=i: self.computer_components[i-1][1].focus_set())
                replace_entry.bind(
                    "<Up>", lambda event, i=i: self.computer_components[i-1][3].focus_set())

            # Bind DOWN key to move down the entry list as long as it's not the last entry.
            if i < len(self.computer_components) - 1:
                entry.bind("<Down>", lambda event,
                           i=i: self.computer_components[i+1][1].focus_set())
                replace_entry.bind(
                    "<Down>", lambda event, i=i: self.computer_components[i+1][3].focus_set())

        # Buttons
        completed_button = tkinter.Button(self, text="Completed", width=14)
        completed_button.grid(row=12, column=0, columnspan=2)

    def load_ticket(self, ticket, ticket_name):
        # check if user is click on the same name or on a different name
        if self.previous_ticket_owner != ticket_name and self.previous_ticket_owner != "":
            all_previous_general_component_values = []
            all_previous_computer_component_values = []

            # get all the previous ticket's entries
            for comp in self.general_components:
                attr_value = comp[-1].get()
                all_previous_general_component_values.append(attr_value)

            for comp in self.computer_components:
                attr_value = comp[-1].get()
                all_previous_computer_component_values.append(attr_value)

            # ============= Initialize Database ===================
            conn = sqlite3.connect('pcbuildsim.db')
            cur = conn.cursor()

            # destructure all general components values
            a, b, c, d, e, f, g, h, i, j, k, l = all_previous_general_component_values
            # destructure all computer components values
            m, n, o, p, q, r, s, t, u = all_previous_computer_component_values

            # save them to database before you do any other thing
            cur.execute("UPDATE Tickets SET name=?, labour=?, budget=?, due_date=?, \
                            new_parts=?, manufacturer=?, dust=?, virus=?, cable_colour=?, \
                            D3Mark=?, will_it_run=?, spec=?, CPU=?, Cooling=?, Motherboard=?, \
                            RAM=?, GPU=?, Storage=?, PSU=?, PCCase=?, Case_Fans=? WHERE name=?",
                        (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, a))
            conn.commit()
            conn.close()

            # refresh the database
            new_model = Model()
            self.controller.model = new_model

        for component in self.general_components:
            if ticket is None:
                component[3].set('')
            attr_value = getattr(ticket, component[2], None)
            # print(attr_value)
            if attr_value is not None:
                component[3].set(attr_value)
            else:
                component[3].set('')

        for component in self.computer_components:
            if ticket is None:
                component[5].set('')
            attr_value = getattr(ticket, component[4], None)
            if attr_value is not None:
                component[5].set(attr_value)
            else:
                component[5].set('')

        self.previous_ticket_owner = ticket_name
        self.previous_ticket = ticket
