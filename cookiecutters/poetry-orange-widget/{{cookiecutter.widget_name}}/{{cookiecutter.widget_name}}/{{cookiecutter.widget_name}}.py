"""{{cookiecutter.widget_name}} Widget

Description.

See:
    - https://orange-development.readthedocs.io/
    - https://orange3.readthedocs.io/projects/orange-development/_modules/orangewidget/widget.html
"""

from Orange.widgets.widget import OWWidget
from Orange.widgets.widget import Input
from Orange.widgets.widget import Output
from Orange.widgets.settings import Setting
from Orange.widgets import gui
from Orange.data import Table

from AnyQt.QtGui import QDoubleValidator


class {{cookiecutter.widget_name}}(OWWidget):
    """Docstring."""

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
            box='Base Settings', valueType=float)

        # --------------------
        # Callbacks (on init)
        # --------------------
        # ...


    # -------------------------------------------------------------------------
    # Transformations
    # -------------------------------------------------------------------------
    def some_transformation(self):
        """Docstring."""

        out_data = self.in_data
        if self.some_setting % 2 == 1:
            out_data.shuffle()

        return out_data


    # -------------------------------------------------------------------------
    # Callbacks
    # -------------------------------------------------------------------------
    @Inputs.in_data
    def set_data(self, in_data):
        """Recieves, validates and process (if needed) the input data."""

        self.in_data = in_data
        self.some_transformation()


    def handleNewSignals(self):
        """
        Invoked by the workflow signal propagation manager after all
        signals handlers have been called.
        Reimplement this method in order to coalesce updates from
        multiple updated inputs.
        """

        pass


    def some_setting_changed(self):
        """Docstring."""

        out_data = self.some_transformation()
        self.Outputs.out_data.send(out_data)