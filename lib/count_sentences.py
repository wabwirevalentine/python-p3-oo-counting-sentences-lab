#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        if not self.value:
            return 0
        
        temp_value = self.value.replace('!', '.').replace('?', '.')
        
        sentences = temp_value.split('.')
        
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return len(sentences)
    pass

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # => 3

string.value = "Hello... World? Yes!"
print(string.count_sentences())  # => 3

string.value = 123  # Will print "The value must be a string." and set to ''
print(string.count_sentences())  # => 0