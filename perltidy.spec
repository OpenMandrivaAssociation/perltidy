Summary:	Script which indents and reformats Perl script
Name:		perltidy
Version:	20101217
Release:	12
License:	GPLv2
Group:		Text tools
Url:		http://perltidy.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/perltidy/Perl-Tidy-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perltidy is a Perl script which indents and reformats Perl scripts to
make them easier to read. If you write Perl scripts, or spend much time
reading them, you will probably find it useful.

%prep
%setup -qn Perl-Tidy-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README COPYING docs
%{_bindir}/*
%{perl_vendorlib}/Perl
%{_mandir}/man1/*
%{_mandir}/man3/*

