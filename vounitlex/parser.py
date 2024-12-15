# Main module for the parser
from enum import StrEnum

from lark import Lark, UnexpectedCharacters, UnexpectedEOF, tree


class VOUnitVersion(StrEnum):
    """Enumeration of supported VOUnit versions"""

    VOUNIT1_1 = "1.1"


class VOUnitParser:
    """A parser for VOUnit strings"""

    def __init__(self, version: VOUnitVersion = VOUnitVersion.VOUNIT1_1):
        self.version = version
        self.parser = Lark.open(
            f"./vounitlex/grammars/vounit{version}.lark",
            start="input",
        )

    def parse(self, string: str) -> tree.Tree:
        """Parse a VOUnit string"""

        return self.parser.parse(string)

    def check(self, string: str) -> bool:
        """Check if a VOUnit string is valid"""
        try:
            self.parser.parse(string)
            return True
        except (UnexpectedEOF, UnexpectedCharacters):
            return False

    def to_dot(self, parsed: tree.Tree, filename: str) -> str:
        """Generate a DOT representation of the parser"""
        return tree.pydot__tree_to_dot(parsed, filename)

    def to_png(self, parsed: tree.Tree, filename: str) -> str:
        """Generate a DOT representation of the parser"""
        return tree.pydot__tree_to_png(parsed, filename)
