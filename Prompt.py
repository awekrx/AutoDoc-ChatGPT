class Prompt:
    def __init__(self, language: str, text: str, example: str = None):
        self.text = text
        self.language = language
        return self

    def create(self) -> str:
        return getattr(self, f"__{self.language}__")(self.create)

    def __py__(self, text: str) -> str:
        return f"""Write class and function Google Style documentations with examples in comments for code:\n{text}\nIn your answer, add comments to the existing code. Don't write anything for yourself."""

    def __example__(self, text: str, example: str) -> str:
        return f"""Write comments:\n{text}\nLike in this example:\n{example}\nIn your answer, add comments to the existing code. Don't write anything for yourself."""
