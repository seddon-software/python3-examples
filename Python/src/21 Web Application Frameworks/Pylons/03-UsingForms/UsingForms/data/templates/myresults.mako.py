# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326571358.773
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\03-UsingForms\\UsingForms\\usingforms\\templates/myresults.mako'
_template_uri='/myresults.mako'
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
        __M_writer(u'</title>\r\n</head>\r\n<body>\r\n\t<h1>Results</h1><hr/>\r\n\t')
        # SOURCE LINE 7
        __M_writer(escape(c.text))
        __M_writer(u'\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


