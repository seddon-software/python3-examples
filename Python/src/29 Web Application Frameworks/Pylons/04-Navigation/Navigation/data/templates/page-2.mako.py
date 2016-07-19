# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326582682.4649999
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\04-Navigation\\Navigation\\navigation\\templates/page-2.mako'
_template_uri='page-2.mako'
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
        __M_writer(u'<html>\r\n<head>\r\n\t<title>PAGE 2</title>\r\n</head>\r\n<body>\r\n\t<h1>This is page 2</h1>\r\n\t<a href="index">refresh</a>\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


