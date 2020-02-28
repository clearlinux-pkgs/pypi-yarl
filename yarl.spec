#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yarl
Version  : 1.4.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/d6/67/6e2507586eb1cfa6d55540845b0cd05b4b77c414f6bca8b00b45483b976e/yarl-1.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/67/6e2507586eb1cfa6d55540845b0cd05b4b77c414f6bca8b00b45483b976e/yarl-1.4.2.tar.gz
Summary  : Yet another URL library
Group    : Development/Tools
License  : Apache-2.0
Requires: yarl-license = %{version}-%{release}
Requires: yarl-python = %{version}-%{release}
Requires: yarl-python3 = %{version}-%{release}
Requires: idna
Requires: multidict
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : multidict

%description
yarl
====

.. image:: https://dev.azure.com/aio-libs/yarl/_apis/build/status/CI?branchName=master
  :target: https://dev.azure.com/aio-libs/yarl/_build/latest?definitionId=7&branchName=master
  :align: right

.. image:: https://codecov.io/gh/aio-libs/yarl/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aio-libs/yarl

.. image:: https://badge.fury.io/py/yarl.svg
    :target: https://badge.fury.io/py/yarl


.. image:: https://readthedocs.org/projects/yarl/badge/?version=latest
    :target: https://yarl.readthedocs.io


.. image:: https://img.shields.io/pypi/pyversions/yarl.svg
    :target: https://pypi.python.org/pypi/yarl

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/aio-libs/Lobby
    :alt: Chat on Gitter

Introduction
------------

Url is constructed from ``str``::

   >>> from yarl import URL
   >>> url = URL('https://www.python.org/~guido?arg=1#frag')
   >>> url
   URL('https://www.python.org/~guido?arg=1#frag')

All url parts: *scheme*, *user*, *password*, *host*, *port*, *path*,
*query* and *fragment* are accessible by properties::

   >>> url.scheme
   'https'
   >>> url.host
   'www.python.org'
   >>> url.path
   '/~guido'
   >>> url.query_string
   'arg=1'
   >>> url.query
   <MultiDictProxy('arg': '1')>
   >>> url.fragment
   'frag'

All url manipulations produce a new url object::

   >>> url.parent / 'downloads/source'
   URL('https://www.python.org/downloads/source')

Strings passed to constructor and modification methods are
automatically encoded giving canonical representation as result::

   >>> url = URL('https://www.python.org/путь')
   >>> url
   URL('https://www.python.org/%D0%BF%D1%83%D1%82%D1%8C')

Regular properties are *percent-decoded*, use ``raw_`` versions for
getting *encoded* strings::

   >>> url.path
   '/путь'

   >>> url.raw_path
   '/%D0%BF%D1%83%D1%82%D1%8C'

Human readable representation of URL is available as ``.human_repr()``::

   >>> url.human_repr()
   'https://www.python.org/путь'

For full documentation please read https://yarl.readthedocs.org.


Installation
------------

::

   $ pip install yarl

The library is Python 3 only!


Dependencies
------------

YARL requires multidict_ library.


API documentation
------------------

The documentation is located at https://yarl.readthedocs.org

Comparison with other URL libraries
------------------------------------

* furl (https://pypi.python.org/pypi/furl)

  The library has rich functionality but the ``furl`` object is mutable.

  I'm afraid to pass this object into foreign code: who knows if the
  code will modify my url in a terrible way while I just want to send URL
  with handy helpers for accessing URL properties.

  ``furl`` has other non-obvious tricky things but the main objection
  is mutability.

* URLObject (https://pypi.python.org/pypi/URLObject)

  URLObject is immutable, that's pretty good.

  Every URL change generates a new URL object.

  But the library doesn't do any decode/encode transformations leaving the
  end user to cope with these gory details.


Source code
-----------

The project is hosted on GitHub_

Please file an issue on the `bug tracker
<https://github.com/aio-libs/yarl/issues>`_ if you have found a bug
or have some suggestion in order to improve the library.

The library uses `Azure Pipelines <https://dev.azure.com/aio-libs/yarl>`_ for
Continuous Integration.

Discussion list
---------------

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Feel free to post your questions and ideas here.


Authors and License
-------------------

The ``yarl`` package is written by Andrew Svetlov.

It's *Apache 2* licensed and freely available.


.. _GitHub: https://github.com/aio-libs/yarl

.. _multidict: https://github.com/aio-libs/multidict


=========
Changelog
=========

..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/#adding-a-news-entry
    we named the news folder "changes".

    WARNING: Don't drop the next directive!

.. towncrier release notes start

1.4.1 (2019-11-29)
==================

* Fix regression, make the library work on Python 3.5 and 3.6 again.

1.4.0 (2019-11-29)
==================

* Distinguish an empty password in URL from a password not provided at all (#262)

* Fixed annotations for optional parameters of ``URL.build`` (#309)

* Use None as default value of ``user`` parameter of ``URL.build`` (#309)

* Enforce building C Accelerated modules when installing from source tarball, use
  ``YARL_NO_EXTENSIONS`` environment variable for falling back to (slower) Pure Python
  implementation (#329)

* Drop Python 3.5 support

* Fix quoting of plus in path by pure python version (#339)

* Don't create a new URL if fragment is unchanged (#292)

* Included in error msg the path that produces starting slash forbidden error (#376)

* Skip slow IDNA encoding for ASCII-only strings (#387)


1.3.0 (2018-12-11)
==================

* Fix annotations for ``query`` parameter (#207)

* An incoming query sequence can have int variables (the same as for
  Mapping type) (#208)

* Add ``URL.explicit_port`` property (#218)

* Give a friendlier error when port cant be converted to int (#168)

* ``bool(URL())`` now returns ``False`` (#272)

1.2.6 (2018-06-14)
==================

* Drop Python 3.4 trove classifier (#205)

1.2.5 (2018-05-23)
==================

* Fix annotations for ``build`` (#199)

1.2.4 (2018-05-08)
==================

* Fix annotations for ``cached_property`` (#195)

1.2.3 (2018-05-03)
==================

* Accept ``str`` subclasses in ``URL`` constructor (#190)

1.2.2 (2018-05-01)
==================

* Fix build

1.2.1 (2018-04-30)
==================

* Pin minimal required Python to 3.5.3 (#189)

1.2.0 (2018-04-30)
==================

* Forbid inheritance, replace ``__init__`` with ``__new__`` (#171)

* Support PEP-561 (provide type hinting marker) (#182)

1.1.1 (2018-02-17)
==================

* Fix performance regression: don't encode enmpty netloc (#170)

1.1.0 (2018-01-21)
==================

* Make pure Python quoter consistent with Cython version (#162)

1.0.0 (2018-01-15)
==================

* Use fast path if quoted string does not need requoting (#154)

* Speed up quoting/unquoting by ``_Quoter`` and ``_Unquoter`` classes (#155)

* Drop ``yarl.quote`` and ``yarl.unquote`` public functions (#155)

* Add custom string writer, reuse static buffer if available (#157)
  Code is 50-80 times faster than Pure Python version (was 4-5 times faster)

* Don't recode IP zone (#144)

* Support ``encoded=True`` in ``yarl.URL.build()`` (#158)

* Fix updating query with multiple keys (#160)

0.18.0 (2018-01-10)
===================

* Fallback to IDNA 2003 if domain name is not IDNA 2008 compatible (#152)

0.17.0 (2017-12-30)
===================

* Use IDNA 2008 for domain name processing (#149)

0.16.0 (2017-12-07)
===================

* Fix raising ``TypeError`` by ``url.query_string()`` after
  ``url.with_query({})`` (empty mapping) (#141)

0.15.0 (2017-11-23)
===================

* Add ``raw_path_qs`` attribute (#137)

0.14.2 (2017-11-14)
===================

* Restore ``strict`` parameter as no-op in ``quote`` / ``unquote``

0.14.1 (2017-11-13)
===================

* Restore ``strict`` parameter as no-op for sake of compatibility with
  aiohttp 2.2

0.14.0 (2017-11-11)
===================

* Drop strict mode (#123)

* Fix ``"ValueError: Unallowed PCT %"`` when there's a ``"%"`` in the url (#124)

0.13.0 (2017-10-01)
===================

* Document ``encoded`` parameter (#102)

* Support relative urls like ``'?key=value'`` (#100)

* Unsafe encoding for QS fixed. Encode ``;`` char in value param (#104)

* Process passwords without user names (#95)

0.12.0 (2017-06-26)
===================

* Properly support paths without leading slash in ``URL.with_path()`` (#90)

* Enable type annotation checks

0.11.0 (2017-06-26)
===================

* Normalize path (#86)

* Clear query and fragment parts in ``.with_path()`` (#85)

0.10.3 (2017-06-13)
===================

* Prevent double URL args unquoting (#83)

0.10.2 (2017-05-05)
===================

* Unexpected hash behaviour (#75)


0.10.1 (2017-05-03)
===================

* Unexpected compare behaviour (#73)

* Do not quote or unquote + if not a query string. (#74)


0.10.0 (2017-03-14)
===================

* Added ``URL.build`` class method (#58)

* Added ``path_qs`` attribute (#42)


0.9.8 (2017-02-16)
==================

* Do not quote ``:`` in path


0.9.7 (2017-02-16)
==================

* Load from pickle without _cache (#56)

* Percent-encoded pluses in path variables become spaces (#59)


0.9.6 (2017-02-15)
==================

* Revert backward incompatible change (BaseURL)


0.9.5 (2017-02-14)
==================

* Fix BaseURL rich comparison support


0.9.4 (2017-02-14)
==================

* Use BaseURL


0.9.3 (2017-02-14)
==================

* Added BaseURL


0.9.2 (2017-02-08)
==================

* Remove debug print


0.9.1 (2017-02-07)
==================

* Do not lose tail chars (#45)


0.9.0 (2017-02-07)
==================

* Allow to quote ``%`` in non strict mode (#21)

* Incorrect parsing of query parameters with %3B (;) inside (#34)

* Fix core dumps (#41)

* tmpbuf - compiling error (#43)

* Added ``URL.update_path()`` method

* Added ``URL.update_query()`` method (#47)


0.8.1 (2016-12-03)
==================

* Fix broken aiohttp: revert back ``quote`` / ``unquote``.


0.8.0 (2016-12-03)
==================

* Support more verbose error messages in ``.with_query()`` (#24)

* Don't percent-encode ``@`` and ``:`` in path (#32)

* Don't expose ``yarl.quote`` and ``yarl.unquote``, these functions are
  part of private API

0.7.1 (2016-11-18)
==================

* Accept not only ``str`` but all classes inherited from ``str`` also (#25)

0.7.0 (2016-11-07)
==================

* Accept ``int`` as value for ``.with_query()``

0.6.0 (2016-11-07)
==================

* Explicitly use UTF8 encoding in setup.py (#20)
* Properly unquote non-UTF8 strings (#19)

0.5.3 (2016-11-02)
==================

* Don't use namedtuple fields but indexes on URL construction

0.5.2 (2016-11-02)
==================

* Inline ``_encode`` class method

0.5.1 (2016-11-02)
==================

* Make URL construction faster by removing extra classmethod calls

0.5.0 (2016-11-02)
==================

* Add cython optimization for quoting/unquoting
* Provide binary wheels

0.4.3 (2016-09-29)
==================

* Fix typing stubs

0.4.2 (2016-09-29)
==================

* Expose ``quote()`` and ``unquote()`` as public API

0.4.1 (2016-09-28)
==================

* Support empty values in query (``'/path?arg'``)

0.4.0 (2016-09-27)
==================

* Introduce ``relative()`` (#16)

0.3.2 (2016-09-27)
==================

* Typo fixes #15

0.3.1 (2016-09-26)
==================

* Support sequence of pairs as ``with_query()`` parameter

0.3.0 (2016-09-26)
==================

* Introduce ``is_default_port()``

0.2.1 (2016-09-26)
==================

* Raise ValueError for URLs like 'http://:8080/'

0.2.0 (2016-09-18)
==================

* Avoid doubling slashes when joining paths (#13)

* Appending path starting from slash is forbidden (#12)

0.1.4 (2016-09-09)
==================

* Add kwargs support for ``with_query()`` (#10)

0.1.3 (2016-09-07)
==================

* Document ``with_query()``, ``with_fragment()`` and ``origin()``

* Allow ``None`` for ``with_query()`` and ``with_fragment()``

0.1.2 (2016-09-07)
==================

* Fix links, tune docs theme.

0.1.1 (2016-09-06)
==================

* Update README, old version used obsolete API

0.1.0 (2016-09-06)
==================

* The library was deeply refactored, bytes are gone away but all
  accepted strings are encoded if needed.

0.0.1 (2016-08-30)
==================

* The first release.

%package license
Summary: license components for the yarl package.
Group: Default

%description license
license components for the yarl package.


%package python
Summary: python components for the yarl package.
Group: Default
Requires: yarl-python3 = %{version}-%{release}

%description python
python components for the yarl package.


%package python3
Summary: python3 components for the yarl package.
Group: Default
Requires: python3-core
Provides: pypi(yarl)

%description python3
python3 components for the yarl package.


%prep
%setup -q -n yarl-1.4.2
cd %{_builddir}/yarl-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582849540
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yarl
cp %{_builddir}/yarl-1.4.2/LICENSE %{buildroot}/usr/share/package-licenses/yarl/629aef675d0010dc7bc7e08ef043868759e5fd09
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yarl/629aef675d0010dc7bc7e08ef043868759e5fd09

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
