import re


def matchRouter(route, original):

    regexVariable = r'(?<=\{)(.*?)(?=\})'
    regexValue = r'(?<=\/)(.*?)(?=\/|$)'
    regexslash = r'\/'
    variables = dict()

    values = re.findall(regexValue, original)

    slashVariables = re.findall(regexslash, route)
    slashValues = re.findall(regexValue, route)

    for index, variable in enumerate(slashValues, start=0):
        var = re.search(regexVariable, variable)
        if var:
            variables[var.group()] = values[index]

    return variables
