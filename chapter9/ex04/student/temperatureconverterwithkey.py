"""
File: temperatureconverterwithkey.py
Converts Fahrenheit to Celsius and back.
Pressing Enter in a field triggers the conversion that uses that field as input.
"""
from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """A window with two fields for converting between Fahrenheit and Celsius."""

    def __init__(self):
        """Sets up the window, labels, input fields, buttons, and Enter key bindings."""
        EasyFrame.__init__(self, title="Temperature Converter")

        # Column headings above the fields
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        # Input/output fields, starting at the freezing point of water
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=1)

        # Buttons: >>>> converts Fahrenheit to Celsius, <<<< does the reverse
        self.addButton(text=">>>>", row=2, column=0, command=self.computeCelsius)
        self.addButton(text="<<<<", row=2, column=1, command=self.computeFahr)

        # Enter key support: pressing Return in a field runs the conversion
        # that takes that field as its input
        self.fahrField.bind("<Return>", lambda event: self.computeCelsius())
        self.celsiusField.bind("<Return>", lambda event: self.computeFahr())

    def computeCelsius(self):
        """Reads Fahrenheit from the left field and displays Celsius in the right field."""
        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)

    def computeFahr(self):
        """Reads Celsius from the right field and displays Fahrenheit in the left field."""
        celsius = self.celsiusField.getNumber()
        fahr = celsius * 9 / 5 + 32
        self.fahrField.setNumber(fahr)


def main():
    """Creates the window and starts the event loop."""
    TemperatureConverter().mainloop()


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()