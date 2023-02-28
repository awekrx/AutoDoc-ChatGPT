from colorama import Fore, Style

RESET = Style.RESET_ALL
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
BOLD = "\033[1m"


class Settings:
    """
    
    This class stores the settings for a program.
    
    Variables:
    - supported_languages (list): A list of supported languages.
    
    Example Usage:
    ```python
    settings = Settings()
    print(settings.supported_languages) # Output: ["py"]
    ```
    
    Note: There are no functions defined in this class.
    """
    supported_languages = ["py"]
