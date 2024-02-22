%define mate_ver	%(echo %{version}|cut -d. -f1,2)

%define libname %mklibname %{name}-extension
%define devname %mklibname %{name}-extension -d

Summary:	Caja extension for customizing the context menu
Name:		caja-actions
Version:	1.28.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+ and LGPLv2+
Url:		https://www.mate-desktop.org/
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	itstool
BuildRequires:	dblatex
BuildRequires:	docbook-utils
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	yelp-tools

Requires:	%{libname} = %{version}-%{release}

%description
This package provides a Caja file manager extension which
allows the user to add arbitrary program to be launched through the
Caja file manager popup menu of selected files.

%files -f %{name}.lang
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

#---------------------------------------------------------------------------

%package -n %{name}-docs
Summary:	Documentations for %{name}
Group:		Graphical desktop/Other
BuildArch:	noarch

%description -n %{name}-docs
This package contains the documentation for %{name}

%files -n %{name}-docs
%doc AUTHORS ChangeLog NEWS README
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg
%{_docdir}/caja-actions/AUTHORS
%{_docdir}/caja-actions/ChangeLog
%{_docdir}/caja-actions/NEWS
%{_docdir}/caja-actions/README
%{_docdir}/caja-actions/COPYING
%{_docdir}/caja-actions/COPYING-DOCS

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries used by %{name}.

%files -n %{libname}
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files for developing with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains headers and shared libraries needed for development
with caja-actions.

%files -n %{devname}
%{_includedir}/caja-actions/

#---------------------------------------------------------------------------

%prep
%autosetup

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-html-manuals \
	--enable-pdf-manuals \
	--enable-deprecated \
	%{nil}
%make_build

%install
%make_install

# clean docs dirs
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2008
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2009
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2010
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2011
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog-2012
rm -f %{buildroot}%{_docdir}/%{name}/MAINTAINERS

# locales
%find_lang %{name} --with-gnome --all-name

