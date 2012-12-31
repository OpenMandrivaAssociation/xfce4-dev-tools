%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Xfce developer tools
Name:		xfce4-dev-tools
Version:	4.10.0
Release:	3
License:	GPLv2+
Group:		Development/Other
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	automake >= 1.10
BuildRequires:	intltool
Requires:	intltool
Obsoletes:	xfce-dev-tools < 4.5.91
Provides:	xfce-dev-tools

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from SVN. In addition, this package contains the
Xfce developer's handbook.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog HACKING NEWS README
%{_bindir}/*
%{_datadir}/xfce4/dev-tools


%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794603
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.2-1
+ Revision: 791030
- update to new version 4.9.2

* Mon Apr 02 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-2
+ Revision: 788876
- reupload

* Sun Apr 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 788586
- update to new version 4.9.1 (Xfce 4.10pre1))
- packages is no more marked as a noarch
- drop old stuff in spec scripts

* Mon Jan 17 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 631317
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 629088
- update to new version 4.7.4

* Sun Oct 31 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 591154
- update to new version 4.7.3

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-3mdv2010.1
+ Revision: 543292
- rebuild for mdv 2010.1

* Tue Oct 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-2mdv2010.0
+ Revision: 455043
- adapt to new URL schemas for Xfce sources

* Tue Sep 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2010.0
+ Revision: 447445
- update to new version 4.7.2

* Mon Aug 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.0-2mdv2010.0
+ Revision: 420551
- update to new version 4.7.0

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349196
- rebuild whole xfce

* Fri Feb 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345490
- update to new version 4.6.0

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333830
- update to new version 4.5.99.1

* Wed Jan 14 2009 Jérôme Soyer <saispo@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329460
- New upstream release

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303452
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Wed Oct 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294005
- Xfce4.6 beta1 is landing on cooker

* Wed Aug 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0.1-5mdv2009.0
+ Revision: 274086
- require intltool

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 4.4.0.1-4mdv2009.0
+ Revision: 262356
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.4.0.1-3mdv2009.0
+ Revision: 256862
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0.1-1mdv2008.1
+ Revision: 109941
- new version
- do not package COPYING file
- spec file clean

* Sat Nov 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-4mdv2008.1
+ Revision: 109706
- obsolete older release
- use upstream name
- new license policy
- use upstream tarball name as a real name

* Tue Sep 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-3mdv2008.0
+ Revision: 89927
- this package is now noarch, as it is containing only text scripts and files

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.0-2mdv2008.0
+ Revision: 32337
- use macros
- spec file clean

