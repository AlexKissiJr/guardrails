class Callback(ABC):
    """Abstract base class for callbacks."""

    @abstractmethod
    def before_prepare(self, runner):
        """Function to be called before the Runner prepares its operations.
        
        Args:
            runner: Instance of the Runner class.
        """
        pass

    @abstractmethod
    def after_prepare(self, runner):
        """Function to be called after the Runner has prepared its operations.
        
        Args:
            runner: Instance of the Runner class.
        """
        pass

    @abstractmethod
    def before_call(self, runner):
        """Function to be called before the Runner makes a call to the LLM API.
        
        Args:
            runner: Instance of the Runner class.
        """
        pass

    @abstractmethod
    def after_call(self, runner):
        """Function to be called after the Runner has made a call to the LLM API.
        
        Args:
            runner: Instance of the Runner class.
        """
        pass
