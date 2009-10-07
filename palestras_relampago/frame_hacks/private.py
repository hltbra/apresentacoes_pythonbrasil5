"""
>>> class Example(object):
...     @private
...     def private_method(self):
...         print 'method privated called'
...
...     def public_method(self):
...         self.private_method()
...         print 'method public called'


>>> example = Example()
>>> example.private_method()
Traceback (most recent call last):
...
AttributeError: 'private_method' is a private method
>>> example.public_method()
method privated called
method public called


>>> def public_method():
...     example.private_method()
>>> public_method()
Traceback (most recent call last):
...
AttributeError: 'private_method' is a private method
"""

from sys import _getframe
from inspect import getframeinfo

def private(method):
    def newmethod(self, *args, **kwargs):
        calling_context = _getframe(1)
        calling_context_name = calling_context.f_code.co_name
        if not calling_context_name in dir(self) or \
           not getattr(self, calling_context_name).func_code == calling_context.f_code:
            raise AttributeError("'%s' is a private method" % method.__name__)
        return method(self, *args, **kwargs)
    return newmethod


if __name__ == '__main__':
  import doctest
  doctest.testmod()
