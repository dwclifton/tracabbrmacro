""" @package AbbrMacro
    @file macro.py
    @brief The AbbrMacro class

    Return an abbr|acronym element with title attribute.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.0
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.wiki.api import parse_args

from genshi.builder import Element

__all__ = ['AbbrMacro']

class AbbrMacro(WikiMacroBase):
    """Return an abbr|acronym element with title attribute."""

    def expand_macro(self, formatter, macro, args):

        args, kw = parse_args(args)

        keys = ('abbr', 'title')
        tags = ('abbr', 'acronym')
        default = 'acronym'

        try:
            for key in keys:
                kw[key] = kw[key].strip()
        except KeyError:
            return system_message('%s: Missing required keyword "%s."' % (macro, key))

        # tag keyword is optional

        if 'tag' in kw:
            tag = kw['tag'].strip()
            if tag not in tags: tag = default
        else:
            tag = default

        return Element(tag)(kw['abbr'], title="%s" % kw['title'])
