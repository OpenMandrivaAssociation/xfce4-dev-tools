%define packagename xdt-autogen

Summary:		Xfce developer tools
Name:			xfce4-dev-tools
Version:		4.4.0
Release:		%mkrel 4
License:		GPLv2+
Group:			Development/Other
URL:			http://www.xfce.org
Source0:		%{name}-%{version}.tar.bz2
BuildRequires:		automake >= 1.9
BuildRequires:		intltool
BuildArch:		noarch
Obsoletes:		xfce-dev-tools
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot

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
%doc AUTHORS COPYING ChangeLog HACKING NEWS README
%{_bindir}/*
%{_datadir}/xfce4/dev-tools