from lark import Lark, tree


adql_parser = Lark.open(
    "vounit1-1.lark",
    start="input",
    maybe_placeholders=False,
)

with open("test_units.txt") as f:
    test_strings = f.readlines()

test_strings = [test_string.strip() for test_string in test_strings]

for test_string in test_strings:
    print(test_string)
    parsed = adql_parser.parse(test_string)
    print(parsed.pretty())