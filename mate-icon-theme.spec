%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE default icons
Name:		mate-icon-theme
Version:	1.26.0
Release:	2
License:	GPLv3 or CC-BY-SA
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	autoconf-archive
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildRequires:	mate-common
Requires:	hicolor-icon-theme

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides the MATE default icons.

%files
%doc COPYING AUTHORS TODO README
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/*x*
%{_iconsdir}/mate/scalable
%dir %{_iconsdir}/menta
%{_iconsdir}/menta/*x*
%ghost %{_iconsdir}/mate/icon-theme.cache
%ghost %{_iconsdir}/menta/icon-theme.cache
%{_iconsdir}/mate/scalable-up-to-32

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-icon-mapping \
	%{nil}
%make_build

%install
%make_install

touch %{buildroot}%{_iconsdir}/mate/icon-theme.cache
touch %{buildroot}%{_iconsdir}/menta/icon-theme.cache


