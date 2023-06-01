#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : libmspub
Version  : 0.1.4
Release  : 11
URL      : https://dev-www.libreoffice.org/src/libmspub-0.1.4.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libmspub-0.1.4.tar.xz
Summary  : Library for parsing the Microsoft Publisher file format structure
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libmspub-bin = %{version}-%{release}
Requires: libmspub-lib = %{version}-%{release}
Requires: libmspub-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
pushd ..
cp -a libmspub-0.1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685639323
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685639323
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmspub
cp %{_builddir}/libmspub-%{version}/COPYING.MPL %{buildroot}/usr/share/package-licenses/libmspub/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pub2raw
/V3/usr/bin/pub2xhtml
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
/usr/share/doc/libmspub/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmspub-0.1.so.1.0.4
/usr/lib64/libmspub-0.1.so.1
/usr/lib64/libmspub-0.1.so.1.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmspub/9744cedce099f727b327cd9913a1fdc58a7f5599
