#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django-debreach
Version  : 2.0.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/c8/d5/b65bb6f0f783439210973a629668ff73f92e7f0fc7c8e9c760bb3ca196f1/django-debreach-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/d5/b65bb6f0f783439210973a629668ff73f92e7f0fc7c8e9c760bb3ca196f1/django-debreach-2.0.1.tar.gz
Summary  : Adds middleware to give some added protection against the BREACH attack in Django.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: django-debreach-license = %{version}-%{release}
Requires: django-debreach-python = %{version}-%{release}
Requires: django-debreach-python3 = %{version}-%{release}
BuildRequires : Django
BuildRequires : buildreq-distutils3

%description
django-debreach
===============
Basic/extra mitigation against the `BREACH attack <http://breachattack.com/>`_
for Django projects.

%package license
Summary: license components for the django-debreach package.
Group: Default

%description license
license components for the django-debreach package.


%package python
Summary: python components for the django-debreach package.
Group: Default
Requires: django-debreach-python3 = %{version}-%{release}

%description python
python components for the django-debreach package.


%package python3
Summary: python3 components for the django-debreach package.
Group: Default
Requires: python3-core
Provides: pypi(django_debreach)

%description python3
python3 components for the django-debreach package.


%prep
%setup -q -n django-debreach-2.0.1
cd %{_builddir}/django-debreach-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584380272
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/django-debreach
cp %{_builddir}/django-debreach-2.0.1/LICENSE %{buildroot}/usr/share/package-licenses/django-debreach/b9c07b01ae0da41e61dbb805b8c3f7e31972b2f9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/django-debreach/b9c07b01ae0da41e61dbb805b8c3f7e31972b2f9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
