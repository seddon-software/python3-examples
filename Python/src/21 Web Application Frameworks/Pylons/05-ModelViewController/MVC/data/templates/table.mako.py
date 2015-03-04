# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326584663.1159999
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\05-ModelViewController\\MVC\\mvc\\templates/table.mako'
_template_uri='/table.mako'
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
        __M_writer(u'<html>\r\n<head>\r\n\t<title>MVC</title>\r\n</head>\r\n<body>\r\n\r\n<h1>TABLE</h2>\r\n<hr/>\r\n<table>\r\n')
        # SOURCE LINE 10
        for (team,points) in c.data:
            # SOURCE LINE 11
            __M_writer(u'    <tr>\r\n     <td>')
            # SOURCE LINE 12
            __M_writer(escape(team))
            __M_writer(u'</td>\r\n     <td>')
            # SOURCE LINE 13
            __M_writer(escape(points))
            __M_writer(u'</td>\r\n    </tr>\r\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'</table>\r\n\r\n<a href="index">Start again</a>\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


