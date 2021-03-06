'''
GenMovie.py
Generated by MiddleKit.
'''

# MK attribute caches for setFoo() methods
_titleAttr = None
_directorsAttr = None
_castAttr = None
_yearAttr = None
_ratingAttr = None


from datetime import date, datetime, time, timedelta
from decimal import Decimal
from MiscUtils.DateParser import parseDateTime, parseDate, parseTime
from MiddleKit.Run.MiddleObject import MiddleObject
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(dirname(__file__))))
from Middle.Video import Video
del sys.path[0]

from MiddleKit.Run.SQLObjectStore import ObjRefError



class GenMovie(Video):

    def __init__(self):
        Video.__init__(self)
        self._year   = None
        self._rating = None


    def year(self):
        return self._year

    def setYear(self, value):
        assert value is not None
        if value is not None:
            if isinstance(value, int):
                value = int(value)
                #if isinstance(value, int):
                #    raise OverflowError(value)
            elif not isinstance(value, int):
                raise TypeError('expecting int type, but got value %r of type %r instead' % (value, type(value)))

        # set the attribute
        origValue = self._year
        self._year = value

        # MiddleKit machinery
        if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
            global _yearAttr
            if _yearAttr is None:
                _yearAttr = self.klass().lookupAttr('year')
                if not _yearAttr.shouldRegisterChanges():
                    _yearAttr = 0
            if _yearAttr:
                # Record that it has been changed
                self._mk_changed = True
                if self._mk_changedAttrs is None:
                    self._mk_changedAttrs = {}  # maps name to attribute
                self._mk_changedAttrs['year'] = _yearAttr  # changedAttrs is a set
                # Tell ObjectStore it happened
                self._mk_store.objectChanged(self)

    def rating(self):
        return self._rating

    def setRating(self, value):
        assert value is not None
        global _ratingAttr
        if _ratingAttr is None:
            _ratingAttr = self.klass().lookupAttr('rating')

        if value is not None:
            if not isinstance(value, str):
                raise TypeError('expecting string type for enum, but got value %r of type %r instead' % (value, type(value)))
            attr = self.klass().lookupAttr('rating')
            if not attr.hasEnum(value):
                raise ValueError('expecting one of %r, but got %r instead' % (attr.enums(), value))

        # set the attribute
        origValue = self._rating
        self._rating = value

        # MiddleKit machinery
        if not self._mk_initing and self._mk_serialNum>0 and value is not origValue:
            # Record that it has been changed
            self._mk_changed = 1
            if self._mk_changedAttrs is None:
                self._mk_changedAttrs = {}  # maps name to attribute
            self._mk_changedAttrs['rating'] = _ratingAttr  # changedAttrs is a set
            # Tell ObjectStore it happened
            self._mk_store.objectChanged(self)

