""" @package AbbrParser
    @file abbrparser.py
    @brief The AbbrParser class

    Subclass of ConfigParser that preserves the case of option names and
    builds a dictionary of name: (value, section) tuples from a file.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date January, 2009
"""

from ConfigParser import ConfigParser

__all__ = ['AbbrParser', 'ConfigParser', 'build_dict']

class AbbrParser(ConfigParser):
    """Subclass of ConfigParser that preserves the case of option names."""

    def optionxform(self, optionstr):
        return optionstr

def build_dict(file, sections):
    """Build a dictionary of name: (value, section) tuples from a file."""

    parser = AbbrParser()
    parser.read(file)
    dict = {}

    for section in sections:
        if parser.has_section(section):
            for (name, value) in parser.items(section):
                dict[name] = (value, section)
    return dict
