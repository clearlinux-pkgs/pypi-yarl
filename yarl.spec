#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yarl
Version  : 1.2.6
Release  : 1
URL      : https://files.pythonhosted.org/packages/43/b8/057c3e5b546ff4b24263164ecda13f6962d85c9dc477fcc0bcdcb3adb658/yarl-1.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/b8/057c3e5b546ff4b24263164ecda13f6962d85c9dc477fcc0bcdcb3adb658/yarl-1.2.6.tar.gz
Summary  : Yet another URL library
Group    : Development/Tools
License  : Apache-2.0
Requires: yarl-python3
Requires: yarl-license
Requires: yarl-python
Requires: idna
Requires: multidict
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : multidict
BuildRequires : pytest-runner

%description
====

%package license
Summary: license components for the yarl package.
Group: Default

%description license
license components for the yarl package.


%package python
Summary: python components for the yarl package.
Group: Default
Requires: yarl-python3

%description python
python components for the yarl package.


%package python3
Summary: python3 components for the yarl package.
Group: Default
Requires: python3-core

%description python3
python3 components for the yarl package.


%prep
%setup -q -n yarl-1.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534605177
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/yarl
cp LICENSE %{buildroot}/usr/share/doc/yarl/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/yarl/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
