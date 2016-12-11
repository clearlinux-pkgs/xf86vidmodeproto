#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86vidmodeproto
Version  : 2.3.1
Release  : 11
URL      : http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-2.3.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-2.3.1.tar.bz2
Summary  : XF86VidMode extension headers
Group    : Development/Tools
License  : MIT
BuildRequires : pkgconfig(xorg-macros)

%description
XFree86 Video Mode Extension
This extension defines a protocol for dynamically configuring modelines and gamma.

%package dev
Summary: dev components for the xf86vidmodeproto package.
Group: Development
Provides: xf86vidmodeproto-devel

%description dev
dev components for the xf86vidmodeproto package.


%prep
%setup -q -n xf86vidmodeproto-2.3.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xf86vm.h
/usr/include/X11/extensions/xf86vmproto.h
/usr/include/X11/extensions/xf86vmstr.h
/usr/lib64/pkgconfig/xf86vidmodeproto.pc
