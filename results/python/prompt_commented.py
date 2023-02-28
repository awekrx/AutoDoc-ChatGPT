class Prompt:
    """
    A class for generating prompts for coding exercises in a specified language.
    
    Arguments:
    
    language (str): A string representing the language of the prompt (e.g. "python")
    text (str): A string representing the code to be used in the prompt.
    example_text (str): Optional. A string representing an example usage of the code in the prompt.
    
    
    """
    def __init__(self, language: str, text: str, example_text: str = ""):
        """
        Initializes a Prompt instance with the given language, code, and example text.
        
        Arguments:
        
        language (str): A string representing the language of the prompt (e.g. "python")
        text (str): A string representing the code to be used in the prompt.
        example_text (str): Optional. A string representing an example usage of the code in the prompt.
        
        
        """
        self.__text = text
        self.__language = language
        self.__example_text = example_text

    def create(self) -> str:
        """
        
        Generates a prompt using the given language, code, and example text.
        
        Arguments: None
        
        Returns:
        
        str: A string representing the prompt, with placeholders for the code and example text filled in.
        """
        if self.__example_text:
            return (
                open(f"./models/{self.__language}.txt", "r")
                .read()
                .replace("CODE", self.__text)
                .replace("EXAMPLE", self.__example_text)
            )
        else:
            return (
                open(f"./models/{self.__language}.txt", "r")
                .read()
                .replace("CODE", self.__text)
            )
