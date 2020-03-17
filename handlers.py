# -*- coding: utf-8 -*-

import re

re_name = re.compile(r'^[w\-\s]{3,40}$')
re_email = re.compile(r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b')


def handle_name(text, context):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_email(text, context):
    matches = re.findall(re_name, text)
    if len(matches) > 0:
        context['email'] = matches[0]
        return True
    else:
        return False

