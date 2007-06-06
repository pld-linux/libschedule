#
Summary:	libschedule library
Name:		libschedule
Version:	0.16
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	da63b0ed460c0f44b9f85774caf3fb0d
URL:		http://gpe.linuxtogo.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libschedule library.

%package devel
Summary:	Header files for libschedule
Group:		Development/Libraries

%description devel
Header files for libschedule.

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
%attr(755,root,root)    %{_libdir}/libschedule.so.0.0.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/gpe/schedule.h
%{_libdir}/libschedule.la
%{_libdir}/libschedule.so
%{_pkgconfigdir}/libschedule.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libschedule.a
