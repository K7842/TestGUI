import sqlite3

class Model:
    def __init__(self):



        self.get_all_tickets()
        self.get_all_cases()
        self.current_ticket = [None, None]




    def get_all_tickets(self):
        with sqlite3.connect("pcbuildsim.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT name, labour, budget, due_date, new_parts, manufacturer, dust, virus, cable_colour, D3Mark, will_it_run, spec, CPU, Cooling, Motherboard, RAM, GPU, Storage, PSU, PCCase, Case_Fans FROM Tickets")
            result = cursor.fetchall()

            self.all_tickets = [Ticket(name, labour, budget, due, new_parts, manufacturer, dust, virus, cable_colour, D3Mark, will_it_run, spec, CPU, Cooling, Motherboard, RAM, GPU, Storage, PSU, PCCase, Case_Fans) for name, labour, budget, due, new_parts, manufacturer, dust, virus, cable_colour, D3Mark, will_it_run, spec, CPU, Cooling, Motherboard, RAM, GPU, Storage, PSU, PCCase, Case_Fans in result]
        
    def get_all_cases(self):
        with sqlite3.connect("pcbuildsim.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Cases")
            result = cursor.fetchall()

            self.all_cases = [Case(manufacturer, SKU, colour, size, miniITX, microATX, SATX, EATX, XLATX, PSUSize, MaxPSULength, MaxGPULength, MaxCPUFanHeight, MaxRadFans, Lighting, Price) for manufacturer, SKU, colour, size, miniITX, microATX, SATX, EATX, XLATX, PSUSize, MaxPSULength, MaxGPULength, MaxCPUFanHeight, MaxRadFans, Lighting, Price in result]

    def get_ticket(self, ticket_name):
        for i, ticket in enumerate(self.all_tickets):
            if ticket.name == ticket_name:
                self.current_ticket = [i, ticket]
        

class Ticket:
    def __init__(self, name, labour, budget, due, new_parts, manufacturer, dust, virus, cable_colour, D3Mark, will_it_run, spec, CPU, Cooling, Motherboard, RAM, GPU, Storage, PSU, PCCase, Case_Fans):
        self.name = name
        self.labour = labour
        self.budget = budget
        self.due = due
        self.new_parts = new_parts
        self.manufacturer = manufacturer
        self.dust = dust
        self.virus = virus
        self.cable_colour = cable_colour
        self.D3Mark = D3Mark
        self.will_it_run = will_it_run
        self.spec = spec
        self.CPU = CPU
        self.Cooling = Cooling
        self.Motherboard = Motherboard
        self.RAM = RAM
        self.GPU = GPU
        self.Storage = Storage
        self.PSU = PSU
        self.PCCase = PCCase
        self.Case_Fans = Case_Fans

class Case:
    def __init__(self, manufacturer, SKU, colour, size, miniITX, microATX, SATX, EATX, XLATX, PSUSize, MaxPSULength, MaxGPULength, MaxCPUFanHeight, MaxRadFans, Lighting, Price):
        self.manufacturer = manufacturer
        self.SKU = SKU
        self.colour = colour
        self.size = size
        self.miniITX = miniITX
        self.microATX = microATX
        self.SATX = SATX
        self.EATX = EATX
        self.XLATX = XLATX
        self.PSUSize = PSUSize
        self.MaxPSULength = MaxPSULength
        self.MaxGPULength = MaxGPULength
        self.MaxCPUFanHeight = MaxCPUFanHeight
        self.MaxRadFans = MaxRadFans
        self.Lighting = Lighting
        self.Price = Price
