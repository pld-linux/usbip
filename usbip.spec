Summary:	USB device sharing system over IP network
Summary(pl.UTF-8):	System współdzielenia urządzeń USB po sieci IP
Name:		usbip
Version:	0.1.7
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/usbip/%{name}-%{version}.tar.gz
# Source0-md5:	d1094b6d4449787864f8be001639232c
URL:		http://usbip.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gcc >= 6:4.0
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	sysfsutils-devel >= 2.0.0
Requires:	%{name}-libs = %{version}-%{release}
# /lib/hwdata/usb.ids (note: only uncompressed file supported)
Requires:	hwdata >= 0.243-2
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
 - USB keyboards and USB mice: use with Linux console and X Window
   System.
 - USB webcams and USB speakers: view webcam, capture image data and
   play some music.
 - USB printers, USB scanners, USB serial converters and USB Ethernet
   interfaces: ok, use fine.

%description -l pl.UTF-8
Projekt USB/IP ma na celu stworzenie ogólnego systemu współdzielenia
urządzeń USB po sieci IP. W celu współdzielenia urządzeń USB między
komputerami z zachowaniem pełnej funkcjonalności, USB/IP obudowuje
żądania SUB w pakiety IP i przesyła je między komputerami. Oryginalne
sterowniki urządzeń USB oraz aplikacje mogą być używane bez żadnych
modyfikacji. Komputer może wykorzystywać zdaln urządzenia USB tak,
jakby były podłączone bezpośrednio. Przykładowe możliwości:
 - urządzenia USB do przechowywania danych: można używać programów
   fdisk, mkfs, mount/umount, operacji na plikach, odtwarzać filmy
   DVD oraz nagrywać nośniki DVD-R
 - klawiatury i myszy USB: można ich używać na linuksowej konsoli oraz
   w systemie X Window
 - kamery i głośniki USB: można oglądać obraz z kamery, robić zdjęcia
   i odtwarzać muzykę
 - drukarki, skanery, konwertery portów szeregowych oraz interfejsy
   sieciowe USB: można ich normalnie używać

%package libs
Summary:	USB/IP library
Summary(pl.UTF-8):	Biblioteka USB/IP
Group:		Libraries

%description libs
USB over IP library.

%description libs -l pl.UTF-8
Biblioteka USB po IP.

%package devel
Summary:	Header files for usbip library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki usbip
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs
which make use of USB/IP.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
wykorzystujących USB/IP.

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
%configure \
	--disable-usbids-install \
	--with-usbids-dir=/lib/hwdata
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libusbip.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc src/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/bind_driver
%attr(755,root,root) %{_bindir}/usbip
%attr(755,root,root) %{_bindir}/usbipd

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libusbip.so
%{_includedir}/usbip

%files libs
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libusbip.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusbip.so.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libusbip.a
