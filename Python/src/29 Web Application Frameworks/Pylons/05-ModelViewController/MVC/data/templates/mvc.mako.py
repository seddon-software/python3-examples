# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326584659.7449999
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\05-ModelViewController\\MVC\\mvc\\templates/mvc.mako'
_template_uri='/mvc.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<head>\r\n\t<title>MVC</title>\r\n</head>\r\n<body>\r\n<h1>MVC Example</h1>\r\nChoose one of these links:<p>\r\n\r\n<a href="display?model=football&view=table">Football as a table</a><br/>\r\n<a href="display?model=football&view=chart">Football as a chart</a><br/>\r\n<a href="display?model=rugby&view=table">Rugby as a table</a><br/>\r\n<a href="display?model=rugby&view=chart">Rugby as a chart</a><br/>\r\n\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


