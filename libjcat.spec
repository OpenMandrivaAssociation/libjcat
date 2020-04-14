%global major 1
%define libname %mklibname jcat %major
%define devname %mklibname -d jcat
%global glib2_version 2.45.8
%global json_glib_version 1.1.1

Summary:   Library for reading Jcat files
Group:     System/Libraries
Name:      libjcat
Version:   0.1.1
Release:   1
License:   LGPLv2+
URL:       https://github.com/hughsie/libjcat
Source0:   https://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gnutls
BuildRequires: vala
BuildRequires: help2man
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gpgme-glib)
BuildRequires: pkgconfig(vapigen)

Requires: glib2%{?_isa} >= %{glib2_version}

%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package -n %libname
Summary: Library for reading Jcat files
Group: System/Libraries

%description -n %libname
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package -n %devname
Group: Development/C
Summary: Development package for %{name}
Requires: %{libname} = %{version}-%{release}

%description -n %devname
Files for development with %{name}.

%package tests
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%setup -q

%build

%meson \
    -Dgtkdoc=true \
    -Dtests=false

%meson_build

%install
%meson_install

%files -n %libname
%doc README.md
%license LICENSE
%{_bindir}/jcat-tool
%{_datadir}/man/man1/*.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libjcat.so.1*

%files -n %devname
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libjcat
%{_includedir}/libjcat-1
%{_libdir}/libjcat.so
%{_libdir}/pkgconfig/jcat.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jcat.deps
%{_datadir}/vala/vapi/jcat.vapi

%files tests
%doc README.md
%dir %{_datadir}/installed-tests
%dir %{_libexecdir}/installed-tests
%dir %{_libexecdir}/installed-tests/libjcat
%{_libexecdir}/installed-tests/libjcat/jcat-self-test
%{_datadir}/installed-tests/libjcat/*
%dir %{_datadir}/installed-tests/libjcat
