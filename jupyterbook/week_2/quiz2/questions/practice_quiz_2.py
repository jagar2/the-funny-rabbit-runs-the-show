from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TrueFalse_style
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f'Which of the following Python data structures allows modification after creation?',
            style=MCQ,
            question_number=1,
            keys=['q1-Data-Structure-Modification', 'q2-Type-Conversion'],
            options=[['- Dictionary', '- Frozenset', '- Tuple', '- String'], ['- 5.14 (Int)', '- 5.14 (Float)', '- 5.14 (String)', '- "3.142"']],
            descriptions=['Which of the following Python data structures allows modification after creation?', 'What would be the output of the following code: `float("3.14") + 2`?'],
            points=[2.0, 2.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f'In Python, the operation `"Hello"[1:3]` includes the character at index 3.',
            style=TrueFalse_style,
            question_number=3,
            keys=['q1-String-Operations', 'q2-List-Uniqueness'],
            descriptions=['In Python, the operation `"Hello"[1:3]` includes the character at index 3.', 'List elements in Python must be unique within the same list.'],
            points=[2.0, 2.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f'Which of the following operations are valid for Python dictionaries?',
            style=MultiSelect,
            question_number=2,
            keys=['q1-Dictionary-Operations', 'q2-List-Methods'],
            descriptions=['Which of the following operations are valid for Python dictionaries?', 'Which of the following list methods modify the list in-place?'],
            options=[['Using a integer as a dictionary key', 'Adding new key-value pairs after creation', 'Using lists as dictionary keys', 'Having duplicate keys in a dictionary'], ['`append()`', '`count()`', '`sort()`', '`index()`']],
            points=[4.0, 4.0],
            grade=['parts'],
        )
