#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : muparser
Version  : 2.2.6.1
Release  : 3
URL      : https://github.com/beltoforion/muparser/archive/v2.2.6.1.tar.gz
Source0  : https://github.com/beltoforion/muparser/archive/v2.2.6.1.tar.gz
Summary  : Mathematical expressions parser library
Group    : Development/Tools
License  : MIT
Requires: muparser-lib = %{version}-%{release}
Requires: muparser-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake

%description
__________
_____   __ __\______   \_____  _______  ______  ____ _______
/     \ |  |  \|     ___/\__  \ \_  __ \/  ___/_/ __ \\_  __ \
|  Y Y  \|  |  /|    |     / __ \_|  | \/\___ \ \  ___/ |  | \/
|__|_|  /|____/ |____|    (____  /|__|  /____  > \___  >|__|
\/                       \/            \/      \/

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
%setup -q -n muparser-2.2.6.1
cd %{_builddir}/muparser-2.2.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604606657
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1604606657
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/muparser
cp %{_builddir}/muparser-2.2.6.1/License.txt %{buildroot}/usr/share/package-licenses/muparser/c7ba597ebcc597818b91c74c0f39a6832c3128a7
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
/usr/include/muParserStack.h
/usr/include/muParserTemplateMagic.h
/usr/include/muParserTest.h
/usr/include/muParserToken.h
/usr/include/muParserTokenReader.h
/usr/lib64/libmuparser.so
/usr/lib64/pkgconfig/muparser.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmuparser.so.2
/usr/lib64/libmuparser.so.2.2.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/muparser/c7ba597ebcc597818b91c74c0f39a6832c3128a7
