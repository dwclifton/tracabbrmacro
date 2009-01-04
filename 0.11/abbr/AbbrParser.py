""" @package AbbrParser
    @file AbbrParser.py
    @brief The AbbrParser class

    Subclass of ConfigParser that preserves the case of option names.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date January, 2009
"""

from ConfigParser import ConfigParser

__all__ = ['AbbrParser', 'ConfigParser']

class AbbrParser(ConfigParser):
    """Subclass of ConfigParser that preserves the case of option names."""

    def optionxform(self, optionstr):
        return optionstr
