from behave import given, when, then
from main import get_roots, check


@given(u"Biquadratic equation solver is running")
def step_impl(context):
    print(u"Step:Biquadratic equation solver is running")

@when(u'a, b, c are "{a}", "{b}", and "{c}"')
def step_impl(context, a, b, c):
    print(u'Step: a, b, c are "{}", "{}", and "{}"'. format(a, b, c))
    b = str(get_roots(int(a), int(b), int(c))).rpartition(']')[0]
    c = b.partition('[')[2]
    context.result = c
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'Result is "{out}"')
def step_impl(context, out):
    if (context.result == str(out)):
        print(u'Step: Result is right: "{}", "{}"'.format(context.result, out))
        pass
    else :
        raise Exception ("Invalid root is returned.")
