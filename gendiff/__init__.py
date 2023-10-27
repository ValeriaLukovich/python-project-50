from gendiff.diff import generate_diff
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


__all__ = (
    "generate_diff",
    "stylish",
    "plain",
    "json_f",
)
