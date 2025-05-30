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
Package metadata (version, authors, etc).
"""

__all__ = ['get_metadata']

import os
import pathlib
import importlib.metadata

import toml

_VERSION = '0.0.1'


def get_metadata():
    """
    Basic package metadata.

    Retrieves package metadata from the current project directory or from
    the installed package.
    """

    here = pathlib.Path(__file__).parent
    pyproj_toml = 'pyproject.toml'
    meta = {}

    for project_dir in (here, here.parent):

        toml_path = str(project_dir.joinpath(pyproj_toml).absolute())

        if os.path.exists(toml_path):

            pyproject = toml.load(toml_path)

            meta = {
                'name': pyproject['tool']['poetry']['name'],
                'version': pyproject['tool']['poetry']['version'],
                'author': pyproject['tool']['poetry']['authors'],
                'license': pyproject['tool']['poetry']['license'],
                'full_metadata': pyproject,
            }

            break

    if not meta:

        try:

            meta = {
                k.lower(): v for k, v in
                importlib.metadata.metadata(here.name).items()
            }

        except importlib.metadata.PackageNotFoundError:

            pass

    meta['version'] = meta.get('version', None) or _VERSION

    return meta


metadata = get_metadata()
__version__ = metadata.get('version', None)
__author__ = metadata.get('author', None)
__license__ = "{{ cookiecutter._license[cookiecutter.license].license_short }}"
