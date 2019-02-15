

class Options:
    def __init__(self, value, text=''):
        self.value = value
        self.text = text

class FormInput:
    def __init__(self, id='', name='', value='', checked='', text='', type='text'):
        self.id = id
        self.name = name
        self.value = value
        self.checked = checked
        self.text = text
        self.type = type

class Navi:
    def __init__(self, title, url='#', ref=[]):
        self.title = title
        self.url = url
        self.ref = ref