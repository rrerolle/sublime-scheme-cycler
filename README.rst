SchemeCycler
============

The purpose of this Sublime Text 2 plugin it to easily cycle through every
available color scheme. This allows choosing a scheme suitable to you mood at
any time.

This plugin is similar to the Camaleon plugin, but only handles Color Schemes,
not UI themes, and doesn't require manually defining a list of schemes.

Installation
============

There is no good reason for not using Package Control:

http://wbond.net/sublime_packages/package_control

Just install Package Control, and select SchemeCycler in the list of available
packages

Usage
=====

You can cycle through color schemes by hitting the ``F8``, and cycle backward
with ``Shift+F8``.

You can also use the command palette, which defines the
``"SchemeCycler: Next Color Scheme"`` and
``"SchemeCycler: Previous Color Scheme"`` commands.

There is no way to select a random scheme. It just doesn't make sense. If you
really need a random scheme, just press ``F8`` a random number of times.

Configuration
=============

To change the keyboard mappings, simply bind the ``next_color_scheme`` and
``previous_color_scheme`` commands to the desired keys.