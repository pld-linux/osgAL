%define _snap 050208
Summary:	osgAL - 3D SoundLibrary for OpenSceneGraph library
Summary(pl):	osgAL - Biblioteka dzwieku 3D dla OpenSceneGraph
Name:		osgAL
Version:	0.3
Release:	0.20%{_snap}.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/osgal/osgal-%{_snap}.tgz
# Source0-md5:	85c149e3f0fa46d7e806374b31af13af
Patch0:		%{name}-occludecallback.patch
URL:		http://www.vrlab.umu.se/research/osgAL/
BuildRequires:	OpenAL++-devel
BuildRequires:	OpenSceneGraph-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
osgAL is a toolkit for handling spatial (3D) sound in the
OpenSceneGraph rendering library.

%description -l pl
osgAL to narzêdzie do obs³ugi d¼wiêku przestrzennego (3D) w
OpenSceneGraph.

%package devel
Summary:	Header files for osgAL library
Summary(pl):	Pliki nag³ówkowe biblioteki osgAL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL++-devel
Requires:	OpenSceneGraph-devel
Requires:	libstdc++-devel

%description devel
Header files for osgAL library.

%description devel -l pl
Pliki nag³ówkowe biblioteki osgAL.

%prep
%setup -q -n %{name}
%patch0 -p1
touch examples/osgalocclude/Makefile.am

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

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.so
%{_libdir}/lib*.la

#%{_libdir}/lib*.a
