#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-yarl
Version  : 1.8.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/c4/1e/1b204050c601d5cd82b45d5c8f439cb6f744a2ce0c0a6f83be0ddf0dc7b2/yarl-1.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/1e/1b204050c601d5cd82b45d5c8f439cb6f744a2ce0c0a6f83be0ddf0dc7b2/yarl-1.8.2.tar.gz
Summary  : Yet another URL library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-yarl-filemap = %{version}-%{release}
Requires: pypi-yarl-lib = %{version}-%{release}
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

%package filemap
Summary: filemap components for the pypi-yarl package.
Group: Default

%description filemap
filemap components for the pypi-yarl package.


%package lib
Summary: lib components for the pypi-yarl package.
Group: Libraries
Requires: pypi-yarl-license = %{version}-%{release}
Requires: pypi-yarl-filemap = %{version}-%{release}

%description lib
lib components for the pypi-yarl package.


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
Requires: pypi-yarl-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(yarl)
Requires: pypi(idna)
Requires: pypi(multidict)

%description python3
python3 components for the pypi-yarl package.


%prep
%setup -q -n yarl-1.8.2
cd %{_builddir}/yarl-1.8.2
pushd ..
cp -a yarl-1.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670500155
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-yarl
cp %{_builddir}/yarl-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-yarl/be9bdf7dee8ceb476456c3675d77e5676c2562e7 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-yarl

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-yarl/be9bdf7dee8ceb476456c3675d77e5676c2562e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
