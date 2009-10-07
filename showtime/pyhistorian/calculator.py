from should_dsl import *
from pyhistorian import *

class Calculator(object):
    def sum(self, n1, n2):
        return n1+n2


class SpecifyingMyNewCalculator(Story):
    """As a lazy mathematician
       I want to use a calculator
       So that I don't waste my time thinking"""
    colored = True
    template_color = 'yellow'
    scenarios = ['SumScenario'] # optional


class SumScenario(Scenario):
    @Given('I have a calculator')
    def set_my_calculator(self):
        self.calculator = Calculator()

    @When('I enter with 1 + 1')
    def sum_one_to_one(self):
        self.result = self.calculator.sum(1, 1)

    @Then('I have $value as result', 2)
    def get_result(self, value):
        self.result |should_be| value


if __name__ == '__main__':
    SpecifyingMyNewCalculator.run()

