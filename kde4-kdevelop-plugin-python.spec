%define		orgname		kdev-python
%define		_kdevelopver	4.7.0
%define		_state		stable
%define		kdever		4.10.0
%define		qtver		4.8.0

Summary:	Python plugins for kdevelop
Summary(pl.UTF-8):	Wtyczki Python dla kdevelop
Name:		kde4-kdevelop-plugin-python
Version:	1.7.0
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}-py3.tar.xz
# Source0-md5:	708e43202056cc241209109b8bbd5bd0
URL:		http://www.kdevelop.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdevelop-pg-qt
BuildRequires:	kde4-kdevplatform-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	python3-devel >= 3.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdevelop >= %{_kdevelopver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python plugins for kdevelop.

%description -l pl.UTF-8
Wtyczki Python dla kdevelop.

%prep
%setup -q -n %{orgname}-%{version}-py3

%build
install -d build
cd build
%cmake \
	../
%{__make}
cd ../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kdevpython --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kdevpython.lang
%defattr(644,root,root,755)
%doc DESIGN README.packagers TODO
%attr(755,root,root) %{_libdir}/kde4/kcm_docfiles.so
%attr(755,root,root) %{_libdir}/kde4/kcm_pep8.so
%attr(755,root,root) %{_libdir}/kde4/kdevpdb.so
%attr(755,root,root) %{_libdir}/kde4/kdevpythonlanguagesupport.so
%attr(755,root,root) %{_libdir}/libkdev4pythoncompletion.so
%attr(755,root,root) %{_libdir}/libkdev4pythonduchain.so
%attr(755,root,root) %{_libdir}/libkdev4pythonparser.so
%{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevpythonsupport
%{_datadir}/config/kdev_python_docfiles.knsrc
%{_datadir}/kde4/services/kcm_kdevpythondocfiles.desktop
%{_datadir}/kde4/services/kcm_kdevpythonpep8.desktop
%{_datadir}/kde4/services/kdevpdb.desktop
%{_datadir}/kde4/services/kdevpythonsupport.desktop
