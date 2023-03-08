class Prompt:
    def __init__(self, language: str, text: str):
        self.__text = text
        self.__language = language

    def create(self) -> str:
        return (
            open(f"./models/{self.__language}.txt", "r")
            .read()
            .replace("CODE", self.__text)
        )
