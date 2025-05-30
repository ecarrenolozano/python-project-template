#!/usr/bin/env python

#
# This file is part of the `{{ cookiecutter.package_name }}` Python module
#
# Copyright {{ cookiecutter.__year }}
# {{ cookiecutter.copyright_holder }}
#
# File author(s): {{ cookiecutter.author_full_name }} ({{ cookiecutter.author_email }})
#
# Distributed under the {{ cookiecutter._license[cookiecutter.license].license_short }} license
# See the file `LICENSE` or read a copy at
{{ '' }}{%- if cookiecutter.license == 'GNU General Public License Version 3' -%}

# https://www.gnu.org/licenses/gpl-3.0.txt

{%- elif cookiecutter.license == 'MIT License' -%}

# https://opensource.org/license/mit

{%- elif cookiecutter.license == 'Apache License Version 2.0' -%}

# https://www.apache.org/licenses/LICENSE-2.0

{%- elif cookiecutter.license == 'BSD 3-Clause License' -%}

# https://opensource.org/license/bsd-3-clause

{%- elif cookiecutter.license == 'BSD 2-Clause License' -%}

# https://opensource.org/license/bsd-2-clause

{%- elif cookiecutter.license == 'ISC License' -%}

# https://opensource.org/license/isc-license-txt

{%- elif cookiecutter.license == 'Unlicense' -%}

# https://unlicense.org/

{%- endif -%}{{ '' }}
#

"""
{{ cookiecutter.short_description }}
"""

__all__ = [
    '__version__',
    '__author__',
]

from ._metadata import __author__, __version__
