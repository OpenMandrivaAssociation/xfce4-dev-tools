%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Xfce developer tools
Name:		xfce4-dev-tools
Version:	4.16.0
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	xfce.macros
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)

Provides:	xfce-dev-tools

Requires:	intltool
Requires:	gtk-doc

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from SVN. In addition, this package contains the
Xfce developer's handbook.

%files
%doc AUTHORS ChangeLog HACKING NEWS README.md
%{_bindir}/*
#{_datadir}/xfce4/dev-tools
%{_sys_macros_dir}/xfce4.macros

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

# rpm helper macros
install -dm 0755 %{buildroot}%{_sys_macros_dir}/
install -pm 0644 %{SOURCE1} %{buildroot}%{_sys_macros_dir}/xfce4.macros
