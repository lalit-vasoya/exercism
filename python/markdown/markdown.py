import re

def parse(markdown):
  
    s = markdown
    s = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', s) #replace __ to <strong>
    s = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', s) #replace _ to <em>
    s = re.sub(r'^\* (.*?$)', r'<li>\1</li>', s, flags=re.M) # \* (string) \*,<ul>\1</ul> 
    s = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', s, flags=re.S) # <li>(<li>string</li>)</li>,<ul>\1</ul> 
    for i in range(6, 0, -1):
        s = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), s, flags=re.M) # ## <h2> ### <h3>..

    s = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', s, flags=re.M)
    s = re.sub(r'\n', '', s)
    return s

