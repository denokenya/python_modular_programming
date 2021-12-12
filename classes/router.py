class router(object):
    
    """A simple class definition

        Parameters:
            {
                name,
                interface_number,
                vendor
            }

    """

    def __init__(self, name, interface_number, vendor):
        self.name = name
        self.interface_number = interface_number
        self.vendor = vendor


r1 = router("SFO1_RI", 64, "Cisco")
print("-"*20)
print()
print("ROUTER DETAILS:\n")
print(f"Router Name:{r1.name} \n")
print(f"Router Interface Number: {r1.interface_number}\n ")
print(f"Router Vendor: {r1.vendor} ")


class newrouter(router):
    name = input("What is router name:\n")
    interface_number = int(input("What is the interface Number:\n"))
    vendor = input("What is the vendor?\n")
    newrouter = router(name, interface_number, vendor)
    print(f"New Router Name :{newrouter.name} ")
    print(f"interface number: {newrouter.interface_number} ")
    print(f"Vendor : {newrouter.vendor} ")
