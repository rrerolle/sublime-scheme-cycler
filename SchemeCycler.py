#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import os


def dirname(path):
    return path.rsplit('/', 1)[0]


def basename(path):
    return path.rsplit('/', 1)[1]


def splitext(path):
    return path.rsplit('.', 1)


def fix_path(path):
    return path.replace('\\', '/')


def cycle_scheme(backward=False):
    package_path = fix_path(sublime.packages_path())

    schemes = ['/'.join([
                fix_path(dirpath[len(dirname(package_path)) + 1:]),
                filename,
            ]
        )
        for dirpath, _, filenames in os.walk(package_path)
        for filename in filenames if filename.endswith('.tmTheme')
    ]
    schemes.sort(key=lambda x: basename(x))
    settings = sublime.load_settings('Preferences.sublime-settings')
    current_scheme = settings.get('color_scheme')
    scheme_index = schemes.index(current_scheme) + (backward and -1 or 1)
    if scheme_index == len(schemes):
        scheme_index = 0
    elif scheme_index == -1:
        scheme_index = len(schemes) - 1
    scheme = schemes[scheme_index]
    if not scheme:
        return
    settings.set('color_scheme', scheme)
    sublime.save_settings('Preferences.sublime-settings')

    sublime.status_message(
        u'Color Scheme: ' + splitext(basename(scheme).decode('utf-8'))[0]
    )


class NextColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme()


class PreviousColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme(backward=True)
