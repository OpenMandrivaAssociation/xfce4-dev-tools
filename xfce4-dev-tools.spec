%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Xfce developer tools
Name:		xfce4-dev-tools
Version:	4.12.0
Release:	2
License:	GPLv2+
Group:		Development/Other
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)

Requires:	intltool
Provides:	xfce-dev-tools

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from SVN. In addition, this package contains the
Xfce developer's handbook.

%files
%doc AUTHORS ChangeLog HACKING NEWS README
%{_bindir}/*
%{_datadir}/xfce4/dev-tools

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install
