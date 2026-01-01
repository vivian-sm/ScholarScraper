import json

class ScholarPaper:
    def __init__(
        self,
        title: str,
        link: str,
        description: str,
        authors: str,
    ):
        self.set_title(title)
        self.set_link(link)
        self.set_description(description)
        self.set_authors(authors)

    def get_title(self) -> str:
        return self.__title

    def get_link(self) -> str:
        return self.__link

    def get_description(self) -> str:
        return self.__description

    def get_authors(self) -> str:
        return self.__authors
    
    def set_title(self, title: str):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        self.__title = title.strip()

    def set_link(self, link: str):
        if not isinstance(link, str) or not link.strip():
            raise ValueError("Link must be a non-empty string.")
        self.__link = link.strip()

    def set_description(self, description: str):
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        self.__description = description.strip()

    def set_authors(self, authors: str):
        if not isinstance(authors, str):
            raise ValueError("Authors must be a string.")
        self.__authors = authors.strip()

    def to_dict(self) -> dict:
        return {
            "title": self.__title,
            "link": self.__link,
            "description": self.__description,
            "authors": self.__authors,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(
            self.to_dict(),
            indent=indent,
            ensure_ascii=False,
        )

    def __str__(self) -> str:
        return (
            f"title: {self.__title}\n"
            f"link: {self.__link}\n"
            f"description: {self.__description}\n"
            f"authors: {self.__authors}"
        )

    def __repr__(self) -> str:
        return (
            f"Paper(title={self.__title!r}, "
            f"link={self.__link!r}, "
            f"authors={self.__authors!r})"
        )
