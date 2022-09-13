__all__ = ['text_validation']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['validate_response'])
@Js
def PyJsHoisted_validate_response_(text, this, arguments, var=var):
    var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
    var.registers(['text'])
    return (var.get('text') and Js(True))
PyJsHoisted_validate_response_.func_name = 'validate_response'
var.put('validate_response', PyJsHoisted_validate_response_)
pass
pass


# Add lib to the module scope
text_validation = var.to_python()