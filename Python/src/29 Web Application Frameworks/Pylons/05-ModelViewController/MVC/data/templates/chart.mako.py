# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326584665.826
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\05-ModelViewController\\MVC\\mvc\\templates/chart.mako'
_template_uri='/chart.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        c = context.get('c', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<head>\r\n\t<title>MVC</title>\r\n</head>\r\n<body>\r\n\r\n<h1>CHART</h2>\r\n<hr/>\r\n<table>\r\n')
        # SOURCE LINE 10
        for (team,points) in c.data:
            # SOURCE LINE 11
            __M_writer(u'\t')
            s = "" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\r\n')
            # SOURCE LINE 12
            for ch in range(int(points)):
                # SOURCE LINE 13
                __M_writer(u'\t\t')
                s += "X" 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 15
            __M_writer(u'    <tr>\r\n     <td>')
            # SOURCE LINE 16
            __M_writer(escape(team))
            __M_writer(u'</td>\r\n     <td>')
            # SOURCE LINE 17
            __M_writer(escape(s))
            __M_writer(u'</td>\r\n    </tr>\r\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'</table>\r\n\r\n<a href="index">Start again</a>\r\n\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


