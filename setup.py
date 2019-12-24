# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '2.2.1'
description = 'A sane, working, editor-friendly way of creating front pages and other composite pages. Working now, for mere mortals.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.cover',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: 5.1',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: JavaScript',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: News/Diary',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone cover javascript dexterity',
      author='Carlos de la Guardia et al.',
      author_email='cguardia@yahoo.com',
      url='https://github.com/collective/collective.cover',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'AccessControl',
          'Acquisition',
          'collective.js.bootstrap',
          'collective.js.galleria',
          'collective.js.jqueryui',
          'collective.z3cform.datetimewidget',
          'Missing',
          'plone.api >=1.4.11',
          'plone.app.blocks >=2.2.1',
          'plone.app.content',
          'plone.app.contentmenu',
          'plone.app.dexterity',
          'plone.app.iterate',
          'plone.app.jquery',
          'plone.app.jquerytools',
          'plone.app.layout',
          'plone.app.linkintegrity',
          'plone.app.lockingbehavior',
          'plone.app.registry',
          'plone.app.textfield',
          'plone.app.tiles >=1.1.0',
          'plone.app.uuid',
          'plone.app.vocabularies',
          'plone.autoform',
          'plone.behavior',
          'plone.dexterity',
          'plone.i18n',
          'plone.indexer',
          'plone.memoize',
          'plone.namedfile',
          'plone.registry',
          'plone.rfc822',
          'plone.scale',
          'plone.supermodel',
          'plone.tiles',
          'plone.uuid',
          'plone.z3cform',
          'Products.CMFCore',
          'Products.CMFPlone >=4.3',
          'Products.GenericSetup',
          'setuptools',
          'six',
          'z3c.caching',
          'z3c.form',
          'zExceptions',
          'zope.annotation',
          'zope.browserpage',
          'zope.component',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.publisher',
          'zope.schema',
          'Zope2',
      ],
      extras_require={
          'relations': [
              'plone.app.dexterity [relations]',
          ],
          'test': [
              'cssselect',
              'lxml',
              'mock',
              'plone.api >=1.8.5',
              'plone.app.robotframework',
              'plone.app.testing [robot]',
              'plone.browserlayer',
              'plone.cachepurging',
              'plone.testing',
              'robotsuite',
              'testfixtures',
              'transaction',
              'tzlocal',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
