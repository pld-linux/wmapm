Summary:	Dockable APM/Battery Monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM dla WindowMakera
Name:		wmapm
Version: 	3.01
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	wmapm.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
WMAPM monitors the APM statistics through the APM support in
the Linux kernel. WMAPM currently provides:
        * Status of power supply (battery or AC);
        * Percentage of battery remaining (numeric and meter);
        * Battery charging status;
        * Time left to battery depletion;
        * High/Low/Critical battery status (Red/Yellow/Green);

%description -l pl
WMAPM monitoruje statystyki APM wykorzystuj±c funkcje zawarte w j±drze
Linuxa. WMAPM dostarcza obecnie nastêpuj±cych informacji:
	* Rodzaj wykorzystywanego ¼ród³a energii (bateria lub zasilacz);
	* D³ugo¶æ ¿ycia baterii (w procentach lub graficznie);
	* Czas pozosta³y do wyczerpania baterii;
	* Stan obci±¿enia baterii;
	* Stan baterii: Wysoki/Niski/Krytyczny (Czerwony/¯ó³ty/Zielony);

%prep
%setup -q

%build
make -C %{name} clean
make -C %{name} \
	COPTS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS CHANGES README HINTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README,HINTS,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%{_applnkdir}/DockApplets/wmapm.desktop
