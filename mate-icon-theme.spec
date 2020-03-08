%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE default icons
Name:		mate-icon-theme
Version:	1.24.0
Release:	1
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
%doc README TODO
%doc COPYING AUTHORS TODO README
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/*x*
%{_iconsdir}/mate/scalable
%dir %{_iconsdir}/menta
%{_iconsdir}/menta/*x*
%ghost %{_iconsdir}/mate/icon-theme.cache
%ghost %{_iconsdir}/menta/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.*
%{_iconsdir}/mate/scalable-up-to-32

#---------------------------------------------------------------------------

%prep
%setup -q

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

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.filter << EOF
^./usr/share/icons/mate/
^./usr/share/icons/menta/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/mate
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/menta
fi
EOF
chmod 0755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.script

%post
%update_icon_cache mate menta

%postun
%clean_icon_cache mate menta

