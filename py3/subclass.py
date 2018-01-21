#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('scratch.meta')


class BaseClass(object):
    def __init_subclass__(cls, *args, **kwargs):
        log.debug('BaseClass.__init_subclass__(cls: {}, args: {}, kwargs: {})'.format(cls, args, kwargs))
        cls.log = logging.getLogger(
            '{}.{}'.format(
                cls.__module__,
                cls.__name__
            )
        )
        cls.__attr__ = f'{cls.__name__}'

        super().__init_subclass__(*args, **kwargs)

class SubClass(BaseClass):
    def __init__(self):
        self.log.debug('{}:__init__()'.format(self.__class__.__name__))
        self.log.debug(f'self.__attr__:{self.__attr__}')

class SubClassSubClass(SubClass):
    def __init__(self):
        self.log.debug(
            '{}:__init__()'.format(
                self.__class__.__name__
            )
        )

if __name__ == '__main__':
    sc = SubClass()
    scsc = SubClassSubClass()
