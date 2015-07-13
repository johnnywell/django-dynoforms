form = {
    'fields': {
        'type': 'dict',
        'propertyschema': {
            'type': 'string',
            'regex': '^\w[_a-z0-9]+',
            'maxlength': 20,
            'required': True
        },
        'valueschema': {
            'type': 'dict'
        },
    },
}
