%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Xfce developer tools
Name:		xfce4-dev-tools
Version:	4.7.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Development/Other
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	automake >= 1.10
BuildRequires:	intltool
Requires:	intltool
BuildArch:	noarch
Obsoletes:	xfce-dev-tools < 4.5.91
Provides:	xfce-dev-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog HACKING NEWS README
%{_bindir}/*
%{_datadir}/xfce4/dev-tools
