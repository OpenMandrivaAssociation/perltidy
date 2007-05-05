%define name    perltidy
%define version 20060719
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Script which indents and reformats Perl script
License:        GPL
Group:          Text tools
Source:         http://prdownloads.sourceforge.net/perltidy/Perl-Tidy-%{version}.tar.bz2
URL:            http://perltidy.sourceforge.net
BuildRequires:  perl-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Perltidy is a Perl script which indents and reformats Perl scripts to
make them easier to read. If you write Perl scripts, or spend much time
reading them, you will probably find it useful.

%prep
%setup -q -n Perl-Tidy-%version
# fix  perms
chmod -R go=u-w *

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING docs
%_bindir/*
%_mandir/*/*
%{perl_vendorlib}/Perl
