# $Id: $

# Authority: dries
# Upstream: Martin Preishuber <Martin.Preishuber@eclipt.at>
# Screenshot: http://www.its4you.at/images/screenshots/log4py.png

%define real_name log4py

Summary: Python logging module similar to log4j
Name: python-log4py
Version: 1.3
Release: 1
License: MIT
Group: Development/Libraries
URL: http://www.its4you.at/english/log4py.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.its4you.at/downloads/files/log4py-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python

%description
Log4Py is a python logging module similar to log4j. It supports logging to
files (including logfile rotation) or to stdout/stderr, variable log-levels,
configurable output formats and configuration via configuration files. 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--prefix="%{_prefix}" \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/* readme.txt log4py.conf
%{_libdir}/python*/site-packages/log4py.py*

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
