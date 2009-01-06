""" @package AbbrMacro
    @file macro.py
    @brief The AbbrMacro class

    Return an <abbr> or <acronym> element with title attribute.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date January, 2009
    @version 0.11.1
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.wiki.api import parse_args

from trac.config import Option
from abbrparser import build_dict

from genshi.builder import Element

__all__ = ['AbbrMacro']

class AbbrMacro(WikiMacroBase):
    """Return an <abbr> or <acronym> element with title attribute."""

    keys = ('key', 'title')
    tags = ('abbr', 'acronym')
    default = 'acronym'

    def expand_macro(self, formatter, macro, args):

        # dictionary file

        section = macro.lower() # [abbr]
        option = 'file'         # file = /path/to/dictionary/file
        dict = {}

        if self.config.has_option(section, option):
            dict = build_dict(self.config.get(section, option), self.tags)

        args, kw = parse_args(args)

        try:
            for key in self.keys:
                kw[key] = kw[key].strip()
        except KeyError:
            if key == 'title' and kw['key'] in dict:
                kw['title'] = dict[kw['key']][0]
                kw['tag'] = dict[kw['key']][1]
            else:
                return system_message('%s: Missing required keyword "%s."' %
                                     (macro, key))
        # tag keyword is optional

        if 'tag' in kw:
            tag = kw['tag'].strip()
            if tag not in self.tags: tag = self.default
        else:
            tag = self.default

        return Element(tag)(kw['key'], title="%s" % kw['title'])
