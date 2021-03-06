#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmspub
Version  : 0.1.4
Release  : 8
URL      : https://dev-www.libreoffice.org/src/libmspub-0.1.4.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libmspub-0.1.4.tar.xz
Summary  : Library for parsing the Microsoft Publisher file format structure
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libmspub-bin = %{version}-%{release}
Requires: libmspub-lib = %{version}-%{release}
Requires: libmspub-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(zlib)
Patch1: fix-build.patch

%description
libmspub is a library and a set of tools for reading and converting MS
Publisher files.

%package bin
Summary: bin components for the libmspub package.
Group: Binaries
Requires: libmspub-license = %{version}-%{release}

%description bin
bin components for the libmspub package.


%package dev
Summary: dev components for the libmspub package.
Group: Development
Requires: libmspub-lib = %{version}-%{release}
Requires: libmspub-bin = %{version}-%{release}
Provides: libmspub-devel = %{version}-%{release}
Requires: libmspub = %{version}-%{release}

%description dev
dev components for the libmspub package.


%package doc
Summary: doc components for the libmspub package.
Group: Documentation

%description doc
doc components for the libmspub package.


%package lib
Summary: lib components for the libmspub package.
Group: Libraries
Requires: libmspub-license = %{version}-%{release}

%description lib
lib components for the libmspub package.


%package license
Summary: license components for the libmspub package.
Group: Default

%description license
license components for the libmspub package.


%prep
%setup -q -n libmspub-0.1.4
cd %{_builddir}/libmspub-0.1.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601862927
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1601862927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmspub
cp %{_builddir}/libmspub-0.1.4/COPYING.MPL %{buildroot}/usr/share/package-licenses/libmspub/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pub2raw
/usr/bin/pub2xhtml

%files dev
%defattr(-,root,root,-)
/usr/include/libmspub-0.1/libmspub/MSPUBDocument.h
/usr/include/libmspub-0.1/libmspub/libmspub.h
/usr/lib64/libmspub-0.1.so
/usr/lib64/pkgconfig/libmspub-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libmspub/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmspub-0.1.so.1
/usr/lib64/libmspub-0.1.so.1.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmspub/9744cedce099f727b327cd9913a1fdc58a7f5599
