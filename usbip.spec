Summary:	USB device sharing system over IP network
Name:		usbip
Version:	0.1.7
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/usbip/%{name}-%{version}.tar.gz
# Source0-md5:	d1094b6d4449787864f8be001639232c
URL:		http://usbip.sourceforge.net/
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	sysfsutils-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}

%description devel
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

This package contains the libraries and header files needed to develop
programs which make use of usbip.

%package static
Summary:	Static usbip library
Summary(pl.UTF-8):	Statyczna biblioteka usbip
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static usbip library.

%description static -l pl.UTF-8
Statyczna biblioteka usbip.

%package client
Summary:	USB/IP client utility
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}

%description client
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

This package contains USB/IP client utility.

%package server
Summary:	USB/IP server utils
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description server
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

This package contains USB/IP client utils.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*so.0

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}d
%attr(755,root,root) %{_bindir}/bind_driver

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/lib*.la
