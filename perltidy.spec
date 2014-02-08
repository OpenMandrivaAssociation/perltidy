%define name    perltidy
%define version 20101217
%define release 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Script which indents and reformats Perl script
License:        GPL
Group:          Text tools
Source:         http://prdownloads.sourceforge.net/perltidy/Perl-Tidy-%{version}.tar.gz
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
#chmod -R go=u-w *

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


%changelog
* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 20101217-2mdv2011.0
+ Revision: 676776
- rebuild

* Mon Dec 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 20101217-1mdv2011.0
+ Revision: 623296
- update to new version 20101217

* Wed Jun 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20090616-1mdv2010.0
+ Revision: 386732
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 20071205-4mdv2009.0
+ Revision: 258653
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20071205-3mdv2009.0
+ Revision: 246645
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20071205-1mdv2008.1
+ Revision: 116181
- update to new version 20071205

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20070801-1mdv2008.0
+ Revision: 63982
- update to new version 20070801

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20070508-1mdv2008.0
+ Revision: 46536
- update to new version 20070508

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 20070504-1mdv2008.0
+ Revision: 23214
- 20070504
- Import perltidy



* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 20060719-1mdv2007.0
- New version 20060719

* Thu Jun 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 20060614-1mdv2007.0
- New version 20060614

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20031021-4mdk 
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 20031021-3mdk 
- rpmbuildupdate aware

* Mon Mar 01 2004 Guillaume Rousse <guillomovitch@mandrake.org> 20031021-2mdk
- fixed dir ownership (distlint)

* Fri Dec 12 2003 Guillaume Rousse <guillomovitch@mandrake.org> 20031021-1mdk
- new version

* Tue Jul 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 20030726-1mdk
- 20030726

* Fri May 23 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 20021130-4mdk
- fixed self-obsolescence (lenny sux)

* Fri May 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 20021130-3mdk
- merge the two perl tidy packages

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 20021130-2mdk
- rebuild

* Sun Dec 01 2002 Lenny Cartier <lenny@mandrakesoft.com> 20021130-1mdk
- 20021130

* Thu Jul 11 2002 Pixel <pixel@mandrakesoft.com> 20020425-3mdk
- rebuild for perl 5.8.0

* Fri Jun 28 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20020425-2mdk 
- fixing list file for arch!=x86

* Mon May 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 20020425-1mdk
- 20020425
- fixed spec (thx Charles Jie)

* Mon Mar 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 20020225-1mdk
- 20020225

* Fri Oct 26 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 20011016-2mdk
- new in contribs

* Thu Oct 18 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 20011016-1mdk
- first Mandrake package  
