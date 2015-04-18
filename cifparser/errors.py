# Copyright 2015 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of cifparser.  cifparser is BSD-licensed software;
# for copyright information see the LICENSE file.

class CifError(Exception):
    "Base exception class for cifparser."
    pass

class ConversionError(CifError):
    "Failed to convert to requested datatype."
    pass
