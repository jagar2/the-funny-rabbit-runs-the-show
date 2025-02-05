from pykubegrader.widgets.select_many import MultiSelect, SelectMany
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-python-lists', 'q2-2-python-dictionaries'],
            descriptions=['Which of the following are true about Python lists?', 'Which of the following are true about Python dictionaries?'],
            options=[['Lists are mutable.', 'Lists can contain elements of different data types.', 'Lists are immutable.', 'Lists can only contain integers.'], ['Dictionaries store key-value pairs.', 'Dictionary keys must be unique.', 'Dictionaries are ordered in modern Python versions.', 'Dictionaries are immutable.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
