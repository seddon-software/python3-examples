import formencode

class MyForm(formencode.Schema):
    filter_extra_fields = True
    allow_extra_fields = True
    firstName = formencode.validators.String(not_empty=True)
    lastName = formencode.validators.String(not_empty=True)
