# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1326569363.138
_template_filename='G:\\Workspace\\Python\\ARM\\src\\Web Front End\\01-StaticPages\\StaticPages\\staticpages\\templates/page2.mako'
_template_uri='page2.mako'
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
        __M_writer(u'This is page 2\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


