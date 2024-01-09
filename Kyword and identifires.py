"""
Python keywords
"""
import keyword
print(keyword.kwlist)

'''
OutPut is:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 
 'with', 'yield']
'''

"""
Identifires 
Rules for Identifiers in Python:
Valid Characters: An identifier can consist of letters (both uppercase and lowercase), digits, 
and underscores _. It must start with a letter (a-z, A-Z) or an underscore (_).

Valid identifier examples: variable_name, _my_var, Var123, myClass

Case Sensitivity: Python is case-sensitive. This means that myVar, myvar, and MYVAR
 are considered different identifiers.

Reserved Keywords: Identifiers cannot be the same as Python keywords or reserved words.
 Keywords are the predefined words in Python that have specific meanings and cannot be used as 
 identifiers.
"""
# Valid identifiers
my_variable = 10
_myVar = 'Hello'
ClassExample = 'Python'

# Invalid identifiers (because they use a reserved keyword 'class')
# class = 'example'
# def = 'function'

