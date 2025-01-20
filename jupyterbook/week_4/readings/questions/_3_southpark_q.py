from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select the Best Answer",
            style=MCQ,
            question_number=1,
            keys=['q1-1-southpark-boolean-evaluation', 'q1-2-boolean-conversion-scenarios'],
            options=[['True', 'False', 'None', 'It raises an error'], ['An empty list `[]`', 'The integer `1`', 'A string containing `Stan`', 'The number `3.14`']],
            descriptions=['What is the result of the following boolean expression in Python?\n```python\ncartman_is_good = False\nbutters_is_kind = True\nprint(cartman_is_good or butters_is_kind)\n```', 'Which of the following values evaluates to `False` in Python?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-logical-negation', 'q3-2-short-circuiting', 'q3-3-equality-checks'],
            descriptions=[None, None, None],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-if-else-logical-operators', 'q2-2-southpark-if-else'],
            descriptions=[None, None],
            options=[['`and`', '`or`', '`not`', '`nor`'], ['When `kenny_alive` is `True`', 'When `kenny_alive` is `False`', 'When the variable `kenny_alive` is undefined', 'Always, regardless of the value of `kenny_alive`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
