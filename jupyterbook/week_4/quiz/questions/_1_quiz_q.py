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
            keys=['q3-1-sensor-failure-conditions', 'q3-2-manufacturing-loop', 'q3-3-temperature-control-break'],
            descriptions=['A sensor failure condition can be checked using an `if` statement to evaluate a condition, such as whether a value exceeds a threshold.', 'A `for` loop can be used to iterate over a sequence of parts in a manufacturing process.', 'In a temperature control system, the `break` statement can be used to stop a loop once the desired temperature is reached.'],
            points=[1.0, 1.0, 1.0],
        )
