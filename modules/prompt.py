class Prompt:
    def __init__(self, language: str, text: str, example_text: str = ""):
        self.__text = text
        self.__language = language
        self.__example_text = example_text

    def create(self) -> str:
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
