from pykubegrader.widgets.true_false import TFQuestion, TFStyle
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-function-scope', 'q3-2-args-order', 'q3-3-optional-arguments'],
            descriptions=['In a smart grid monitoring system, variables declared inside a function are accessible outside the function.', 'In Python, positional arguments must always come before `*args` in a function definition.', 'Optional arguments must have default values.'],
            points=[1.0, 1.0, 1.0],
        )
