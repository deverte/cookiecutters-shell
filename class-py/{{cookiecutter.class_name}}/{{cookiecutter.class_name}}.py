class {{cookiecutter.class_name}}:
    """A one line summary of the class.

    Overall class description (it can consist of several lines).

    Attributes:
        some_property: A `some_property` description.
    """
    
    __some_property = 'Some property default value'

    def __init__(self, some_property):
        """Inits {{cookiecutter.class_name}} one line description."""
        self.some_property = some_property
    
    def some_method(self):
        """A One line summary of the method in descriptive style (e.g. `fetches...`, not `fetch...`)

        Overall function description (it can consist of several lines).

        Args:
            arg: An `arg` description.
            *args: An `*args` description.
            **kwargs: A `**kwargs` description.

        Returns:
            Returns description (obligatory if exists). For
            example (optional):

            {'some_key_1': 'Some value 1',
            'some_key_2': 'Some value 2'}

        Raises:
            SomeException: A `SomeException` description.
        """
        pass
        
    def _some_internal_method(self):
        pass
     
    def __some_private_method(self):
        pass

    @property
    def some_property(self):
        return self.__some_property

    @some_property.setter
    def some_property(self, value):
        self.__some_property = value