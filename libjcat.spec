%define major 1
%define gmajor 1.0
%define libname %mklibname jcat
%define oldlibname %mklibname jcat 1
%define devname %mklibname -d jcat
%define girname %mklibname jcat-gir
%define oldgirname %mklibname jcat-gir 1.0
%global glib2_version 2.45.8
%global json_glib_version 1.1.1

Summary:	Library for reading Jcat files
Group:		System/Libraries
Name:		libjcat
Version:	0.2.3
Release:	1
License:	LGPLv2+
URL:		https://github.com/hughsie/libjcat
Source0:    https://github.com/hughsie/libjcat/releases/download/%{version}/libjcat-%{version}.tar.xz
#Source0:	https://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	gnutls
BuildRequires:	vala
BuildRequires:	help2man
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gpgme-glib)
BuildRequires:  pkgconfig(gmp)
BuildRequires:	pkgconfig(vapigen)
Conflicts:	%{_lib}jcat1 < 0.1.8

%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package -n %{libname}
Summary:	Library for reading Jcat files
Group:		System/Libraries
%rename  %{oldlibname}

%description -n %{libname}
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package -n %{girname}
Summary:	GObject Introspection interface description for Jcat
Group:		System/Libraries
%rename %{oldgirname}
Requires:	%{libname} = %{EVRD}
Conflicts:	%{_lib}jcat1 < 0.1.8

%description -n %{girname}
GObject Introspection interface description for Jcat.

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson \
    -Dgtkdoc=true \
    -Dtests=false

%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/jcat-tool
%{_datadir}/man/man1/*.1*

%files -n %{libname}
%{_libdir}/libjcat.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Jcat-%{gmajor}.typelib

%files -n %{devname}
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libjcat
%{_includedir}/libjcat-1
%{_libdir}/libjcat.so
%{_libdir}/pkgconfig/jcat.pc
%{_datadir}/vala/vapi/jcat.deps
%{_datadir}/vala/vapi/jcat.vapi
