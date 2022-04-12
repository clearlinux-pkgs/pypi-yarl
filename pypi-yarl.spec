#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-yarl
Version  : 1.7.2
Release  : 29
URL      : https://files.pythonhosted.org/packages/f6/da/46d1b3d69a9a0835dabf9d59c7eb0f1600599edd421a4c5a15ab09f527e0/yarl-1.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/f6/da/46d1b3d69a9a0835dabf9d59c7eb0f1600599edd421a4c5a15ab09f527e0/yarl-1.7.2.tar.gz
Summary  : Yet another URL library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-yarl-license = %{version}-%{release}
Requires: pypi-yarl-python = %{version}-%{release}
Requires: pypi-yarl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(idna)
BuildRequires : pypi(multidict)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
yarl
====
.. image:: https://github.com/aio-libs/yarl/workflows/CI/badge.svg
:target: https://github.com/aio-libs/yarl/actions?query=workflow%3ACI
:align: right

%package license
Summary: license components for the pypi-yarl package.
Group: Default

%description license
license components for the pypi-yarl package.


%package python
Summary: python components for the pypi-yarl package.
Group: Default
Requires: pypi-yarl-python3 = %{version}-%{release}

%description python
python components for the pypi-yarl package.


%package python3
Summary: python3 components for the pypi-yarl package.
Group: Default
Requires: python3-core
Provides: pypi(yarl)
Requires: pypi(idna)
Requires: pypi(multidict)

%description python3
python3 components for the pypi-yarl package.


%prep
%setup -q -n yarl-1.7.2
cd %{_builddir}/yarl-1.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649798113
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-yarl
cp %{_builddir}/yarl-1.7.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-yarl/be9bdf7dee8ceb476456c3675d77e5676c2562e7
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-yarl/be9bdf7dee8ceb476456c3675d77e5676c2562e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
