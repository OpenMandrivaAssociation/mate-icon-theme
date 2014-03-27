%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE default icons
Name:		mate-icon-theme
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildRequires:	mate-common
Requires:	hicolor-icon-theme

%description
MATE default icons

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--enable-icon-mapping

%make

%install
%makeinstall_std
touch %{buildroot}%{_iconsdir}/mate/icon-theme.cache

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
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.script

%post
%update_icon_cache mate menta

%postun
%clean_icon_cache mate menta

%files
%doc README TODO
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/*x*
%{_iconsdir}/mate/scalable
%dir %{_iconsdir}/menta
%{_iconsdir}/menta/*x*
%ghost %{_iconsdir}/mate/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.*

%files devel
%{_datadir}/pkgconfig/%{name}.pc

