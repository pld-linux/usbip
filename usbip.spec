Summary:	USB device sharing system over IP network
Name:		usbip
Version:	0.1.7
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/usbip/%{name}-%{version}.tar.gz
# Source0-md5:	d1094b6d4449787864f8be001639232c
URL:		http://usbip.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	sysfsutils-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their
full functionality, USB/IP encapsulates "USB requests" into IP packets
and transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
 - USB storage devices: fdisk, mkfs, mount/umount, file operations,
   play a DVD movie and record a DVD-R media.
 - USB keyboards and USB mice: use with linux console and X Window
   System.
 - USB webcams and USB speakers: view webcam, capture image data and
   play some music.
 - USB printers, USB scanners, USB serial converters and USB Ethernet
   interfaces: ok, use fine.

%package devel
Summary:	Development files for usbip
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the libraries and header files needed to develop
programs which make use of usbip.

%package libs
Summary:	USB/IP library
Group:		Libraries

%description libs
USB over IP library.

%package static
Summary:	Static usbip library
Summary(pl.UTF-8):	Statyczna biblioteka usbip
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static usbip library.

%description static -l pl.UTF-8
Statyczna biblioteka usbip.

%prep
%setup -q

%build
cd src
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc src/AUTHORS src/README
%attr(755,root,root) %{_bindir}/bind_driver
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%files libs
%doc NEWS README
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
