from colorama import Fore, Style

RESET = Style.RESET_ALL
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
BOLD = "\033[1m"


class Settings:
    supported_languages = ["py", "ts", "js"]
    divide_start = {
        "py": r"(?<!.)(class|def)",
        "ts": r"(?<!.)(class|function|interface|type|export)",
        "js": r"(?<!.)(class|function|export)",
    }
    divide_end = {
        "py": r"\n(def|class)",
        "ts": r"\n(function|class|interface|type|export)",
        "js": r"\n(function|class|export)",
    }
