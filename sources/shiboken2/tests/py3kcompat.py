# -*- coding: utf-8 -*-

#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

# Copy of ../../pyside2/tests/util/py3kcompat.py

import sys

IS_PY3K = sys.version_info[0] == 3

if IS_PY3K:
    def b(s):
        if type(s) == bytes:
            return s
        return bytes(s, "UTF8")

    def buffer_(s):
        if s == None:
            return None
        elif type(s) == str:
            return bytes(s, "UTF8")
        elif type(s) == bytes:
            return s
        else:
            memoryview(s)

    def l(n):
        return n

    def unicode_(s):
        return s

    unicode = str
    unichr = chr
    long = int
    unichr = chr
    buffer = buffer_
else:
    def b(s):
        return s

    def l(n):
        return long(n)

    def unicode_(s):
        if type(s) == str:
            import codecs
            c = codecs.lookup('utf-8')
            s2 = c.decode(s, 'ignore')
            return s2[0]
        return u'%s' % s

    unicode = unicode
    unichr = unichr
    long = long
    buffer = buffer
