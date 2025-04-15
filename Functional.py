# a function parameterized with keyword args both specified and unspecified
def doit(a="blah", b="blech", **residual):

    print(f"This is a test... a: {a}; b: {b}")


# a list of dictionaries with parameters for multiple calls of `doit`
dict_list = [
    {"a": 1, "b": 2, "c": -1},
    {"a": "foo", "b": "bar"},
    {"b": "hmm"},
]

# map over the list
results = list(map(lambda d: doit(**d), dict_list))

print(results)
