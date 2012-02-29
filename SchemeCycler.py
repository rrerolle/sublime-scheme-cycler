#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import os.path
import glob


def cycle_scheme(backward=False):
    schemes_path = os.path.join(
        sublime.packages_path(),
        'Color Scheme - Default',
    )
    schemes = [
        os.path.basename(s)
        for s in glob.glob(os.path.join(schemes_path, '*.tmTheme'))
    ]
    settings = sublime.load_settings('Preferences.sublime-settings')
    current_scheme = os.path.basename(settings.get('color_scheme'))
    scheme_index = schemes.index(current_scheme) + (backward and -1 or 1)
    if scheme_index == len(schemes):
        scheme_index = 0
    elif scheme_index == -1:
        scheme_index = len(schemes) - 1
    scheme = schemes[scheme_index]
    if not scheme:
        return
    settings.set(
        'color_scheme',
        os.path.join('Packages', 'Color Scheme - Default', scheme),
    )
    sublime.save_settings('Preferences.sublime-settings')

    sublime.status_message(
        u'Color Scheme: ' + os.path.splitext(scheme.decode('utf-8'))[0]
    )


class CycleSchemeForwardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme()


class CycleSchemeBackwardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_scheme(backward=True)
