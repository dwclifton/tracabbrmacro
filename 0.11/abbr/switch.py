kw = {
    'abbr'   : ' PEP',
    'phrase' : 'Python Enhancement Proposal ',
    'tag'    : 'achronym'
}

keys = ('abbr', 'phrase')
tags = ('abbr', 'acronym')
default = 'acronym'

try:
    for key in keys:
        kw[key] = kw[key].strip()
except KeyError:
    print 'Error: missing keyword %s.' % key

if 'tag' in kw:
    tag = kw['tag'].strip()
    if tag not in tags:
        tag = default
else:
    tag = default

print repr(kw)
print 'tag = %s' % tag
"""
    if key == 'abbr':
        abbr = kw[key].strip()
    elif key == 'phrase':
        phrase = kw[key].strip()
    elif key == 'tag':
        if key in kw and key in tags:
            tag = tags[key].strip()
        else:
            tag = default
"""
