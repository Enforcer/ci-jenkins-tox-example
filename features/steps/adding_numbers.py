from behave import given, when, then
from example import add_function

@given(u'We had numbers "{num1}" and "{num2}"')
def step_impl(context, num1, num2):
    context.numbers = [int(num1), int(num2)]

@when(u'We add one number to another')
def step_impl(context):
    context.result = add_function(*context.numbers)

@then(u'We will get a "{result}"')
def step_impl(context, result):
    assert context.result == int(result)

