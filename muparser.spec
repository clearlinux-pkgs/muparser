#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : muparser
Version  : 2.3.4
Release  : 4
URL      : https://github.com/beltoforion/muparser/archive/v2.3.4/muparser-2.3.4.tar.gz
Source0  : https://github.com/beltoforion/muparser/archive/v2.3.4/muparser-2.3.4.tar.gz
Summary  : Mathematical expressions parser library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: muparser-lib = %{version}-%{release}
Requires: muparser-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://travis-ci.org/beltoforion/muparser.svg?branch=master
:target: https://travis-ci.org/beltoforion/muparser

%package dev
Summary: dev components for the muparser package.
Group: Development
Requires: muparser-lib = %{version}-%{release}
Provides: muparser-devel = %{version}-%{release}
Requires: muparser = %{version}-%{release}

%description dev
dev components for the muparser package.


%package lib
Summary: lib components for the muparser package.
Group: Libraries
Requires: muparser-license = %{version}-%{release}

%description lib
lib components for the muparser package.


%package license
Summary: license components for the muparser package.
Group: Default

%description license
license components for the muparser package.


%prep
%setup -q -n muparser-2.3.4
cd %{_builddir}/muparser-2.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715284143
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1715284143
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/muparser
cp %{_builddir}/muparser-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/muparser/2318aa7efd2d10d6db6898e52e9c2d1a9715b0ab || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/muParser.h
/usr/include/muParserBase.h
/usr/include/muParserBytecode.h
/usr/include/muParserCallback.h
/usr/include/muParserDLL.h
/usr/include/muParserDef.h
/usr/include/muParserError.h
/usr/include/muParserFixes.h
/usr/include/muParserInt.h
/usr/include/muParserTemplateMagic.h
/usr/include/muParserTest.h
/usr/include/muParserToken.h
/usr/include/muParserTokenReader.h
/usr/lib64/cmake/muparser/muparser-targets-relwithdebinfo.cmake
/usr/lib64/cmake/muparser/muparser-targets.cmake
/usr/lib64/cmake/muparser/muparserConfig.cmake
/usr/lib64/cmake/muparser/muparserConfigVersion.cmake
/usr/lib64/libmuparser.so
/usr/lib64/pkgconfig/muparser.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmuparser.so.2
/usr/lib64/libmuparser.so.2.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/muparser/2318aa7efd2d10d6db6898e52e9c2d1a9715b0ab
