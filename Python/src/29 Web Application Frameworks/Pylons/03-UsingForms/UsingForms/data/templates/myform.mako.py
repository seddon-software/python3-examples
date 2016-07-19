# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326580164.362
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\03-UsingForms\\UsingForms\\usingforms\\templates/myform.mako'
_template_uri='/myform.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<head>\r\n\t<title>')
        # SOURCE LINE 3
        __M_writer(escape(c.title))
        __M_writer(u'</title>\r\n</head>\r\n<body>\r\n\t')
        # SOURCE LINE 6
        __M_writer(escape(c.text))
        __M_writer(u'<br>\r\n\t<form action=results>\r\n\t\tFirst Name:<input type="text" name="firstName" /><br/>\r\n\t\tLast Name:<input type="text" name="lastName" /><br/>\r\n\t\t<input type="submit" value="Submit" />\r\n\t</form>\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


