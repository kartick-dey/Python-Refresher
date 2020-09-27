class Device:
    """
    This is the device class.
    """
    def __init__(self, name: str, connected_by: str):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected = False

class Printer(Device):
    """
    This is the printer class which inherites the property of Device class.
    """
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __repr__(self):
        return f"<{super().__str__()} ({self.remaining_pages} pages remain)>"

    def printPages(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return

        print(f"Printing {pages} pages")
        self.remaining_pages = pages


printer = Printer('Printer', "USB", 2000)
printer.printPages(500)
print(printer)

printer.disconnected()
printer.printPages(200)
