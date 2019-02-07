#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : muparser
Version  : 2.2.6.1
Release  : 1
URL      : https://github.com/beltoforion/muparser/archive/v2.2.6.1.tar.gz
Source0  : https://github.com/beltoforion/muparser/archive/v2.2.6.1.tar.gz
Summary  : A fast math parser library
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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549559347
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1549559347
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/muparser
cp License.txt %{buildroot}/usr/share/package-licenses/muparser/License.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmuparser.so
/usr/lib64/pkgconfig/muparser.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmuparser.so.2
/usr/lib64/libmuparser.so.2.2.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/muparser/License.txt
