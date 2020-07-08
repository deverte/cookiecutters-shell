from Orange.widgets.widget import OWWidget
from Orange.widgets.widget import Input
from Orange.widgets.widget import Output
from Orange.widgets.settings import Setting
from Orange.widgets import gui
from Orange.data import Table

from AnyQt.QtGui import QDoubleValidator


class {{cookiecutter.widget_name}}(OWWidget):
    """Docstring"""

    # -------------------------------------------------------------------------
    # Widget info
    # -------------------------------------------------------------------------
    name = '{{cookiecutter.widget_name}}'
    description = 'Widget description'
    # icon = 'Widget icon'


    # -------------------------------------------------------------------------
    # Widget settings (variables)
    # -------------------------------------------------------------------------
    some_setting = Setting(0.5)


    # -------------------------------------------------------------------------
    # Inputs and Outputs
    # -------------------------------------------------------------------------
    class Inputs:
        in_data = Input('Data', Table)


    class Outputs:
        out_data = Output('Data', Table)
    

    # -------------------------------------------------------------------------
    # GUI
    # -------------------------------------------------------------------------
    want_main_area = False
    resizing_enabled = False


    # -------------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------------
    def __init__(self):
        """Defines GUI and on-init callbacks."""

        super().__init__()

        # --------------------
        # GUI
        # --------------------
        gui.lineEdit(
            self.controlArea, self, 'some_setting', 'label', callback=self.some_setting_changed,
            box='Base Settings', valueType=float, validator=QDoubleValidator())

        # --------------------
        # Callbacks (on init)
        # --------------------
        # ...


    # -------------------------------------------------------------------------
    # Transformations
    # -------------------------------------------------------------------------
    def some_transformation(self):
        """Docstring"""

        # --------------------
        # Data transformations
        # --------------------
        out_data = self.in_data
        if self.some_setting % 2 == 1:
            out_data.shuffle()

        # --------------------
        # Outputs
        # --------------------
        self.Outputs.out_data.send(out_data)


    # -------------------------------------------------------------------------
    # Callbacks
    # -------------------------------------------------------------------------
    @Inputs.in_data
    def set_data(self, in_data):
        """Recieves and validates the input data."""

        self.in_data = in_data
        self.some_transformation()


    def some_setting_changed(self):
        """Docstring"""

        self.some_transformation()