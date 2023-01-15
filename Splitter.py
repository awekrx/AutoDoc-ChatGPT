class Splitter:
    separators = {
        "py": ["class", "def"]
    }

    def __init__(self, code: str, language: str):
        self.code = code
        self.content = code
        self.splitted_content = []
        self.language = language

    def split(self, ) -> list[str]:
        return getattr(self, f"__{self.language}__")()

    def __py__(self) -> list:
        def find(content, start=-0):
            index = 10 ** 10
            keyword = ""
            for separator in self.separators["py"]:
                try:
                    if start:
                        separator_index = content.index(
                            separator + " ", start + 1)
                    else:
                        separator_index = content.index(separator + " ")
                    if separator_index < index:
                        index = separator_index
                        keyword = separator
                except:
                    pass
            return index, keyword

        last_class = False
        while True:
            index_start = 0
            index_end = 0
            keyword = ""

            index_start, keyword = find(self.content)
            index_end, _ = find(self.content, index_start)

            if index_start == 10 ** 10 and index_end == 10 ** 10:
                break

            if last_class:
                self.splitted_content[-1] += self.content[index_start:index_end]
                last_class = False
            else:
                self.splitted_content.append(
                    self.content[index_start:index_end])
            self.content = self.content[index_start + 1:]

            if keyword == "class":
                last_class = True
        return self.splitted_content
