# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Piece

Summary: Object Oriented time objects
Name: perl-Time-Piece
Version: 1.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Piece/

Source: http://www.cpan.org/modules/by-module/Time/Time-Piece-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module contains Object Oriented time objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Time/
%{perl_vendorarch}/Time/Piece.pm
%{perl_vendorarch}/Time/Seconds.pm
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/Piece/

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
