Summary:	MATE default icons
Name:		mate-icon-theme
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}/%{name}-%{version}.tar.xz
BuildArch: noarch

#BuildRequires: gtk+2.0
BuildRequires: mate-common
#BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils
BuildRequires: intltool

Requires:	hicolor-icon-theme
#Requires(post,postun):	gtk+2.0

%description
MATE default icons

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--enable-icon-mapping

%make

%install
%makeinstall_std
touch %buildroot%{_datadir}/icons/mate/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.filter << EOF
^./usr/share/icons/mate/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/mate
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.script

%post
%update_icon_cache mate

%postun
%clean_icon_cache mate

%files
%doc README TODO
%dir %{_datadir}/icons/mate
%{_datadir}/icons/mate/*x*
%ghost %{_datadir}/icons/mate/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-mate.*

%files devel
%_datadir/pkgconfig/%name.pc
