Summary:	GPE event scheduling library
Summary(pl.UTF-8):	Biblioteka planowania zdarzeń GPE
Name:		libschedule
Version:	0.16
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	da63b0ed460c0f44b9f85774caf3fb0d
Patch0:		%{name}-link.patch
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libgpewidget-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE event scheduling library.

%description -l pl.UTF-8
Biblioteka planowania zdarzeń GPE.

%package devel
Summary:	Header files for libschedule
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libschedule
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	sqlite-devel

%description devel
Header files for libschedule.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libschedule.

%package static
Summary:	Static libschedule library
Summary(pl.UTF-8):	Statyczna biblioteka libschedule
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libschedule library.

%description static -l pl.UTF-8
Statyczna biblioteka libschedule.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libschedule.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libschedule.so
%{_libdir}/libschedule.la
%{_includedir}/gpe/schedule.h
%{_pkgconfigdir}/libschedule.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libschedule.a
