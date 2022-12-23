from behave import given, then
from main import get_roots, get_roots_biquadratic

@given('I put coefficients {coefficients} into the function')
def step_impl(context, coefficients: str):
    coefficients = list(map(int, coefficients.replace("[", "").replace("]", "").split(", ")))

    context.result = get_roots_biquadratic(get_roots(coefficients[0], coefficients[1], coefficients[2]))


@then('I get roots {result}')
def step_impl(context, result: str):
    if result != '[]':
        result = list(map(float, result.replace("[", "").replace("]", "").split(", ")))
        assert context.result == result

    else:
        assert context.result == []