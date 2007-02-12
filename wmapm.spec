Summary:	Dockable APM/Battery Monitor for WindowMaker
Summary(pl.UTF-8):   Dokowalny monitor APM dla WindowMakera
Summary(pt_BR.UTF-8):   Aplicativo do dock do WindowMaker para monitorar a carga da bateria
Summary(es.UTF-8):   Una aplicación para monitorar la batería en el dock del WindowMaker
Name:		wmapm
Version:	3.1
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	5a62620d49b5cc4c2250e013149ca1e9
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMAPM monitors the APM statistics through the APM support in
the Linux kernel. WMAPM currently provides:
- Status of power supply (battery or AC);
- Percentage of battery remaining (numeric and meter);
- Battery charging status;
- Time left to battery depletion;
- High/Low/Critical battery status (Red/Yellow/Green);

%description -l pl.UTF-8
WMAPM monitoruje statystyki APM wykorzystując funkcje zawarte w jądrze
Linuksa. WMAPM dostarcza obecnie następujących informacji:
- Rodzaj wykorzystywanego źródła energii (bateria lub zasilacz);
- Długość życia baterii (w procentach lub graficznie);
- Czas pozostały do wyczerpania baterii;
- Stan obciążenia baterii;
- Stan baterii: Wysoki/Niski/Krytyczny (Czerwony/Żółty/Zielony);

%description -l pt_BR.UTF-8
Aplicativo do dock do WindowMaker para monitorar a carga da bateria,
através do suporte APM do kernel. Esta informação é útil para
usuários de laptops.

%description -l es.UTF-8
Aplicación para monitorar la batería en el dock del WindowMaker.
Basado en soporte APM del kernel. Es útil en notebooks.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
	COPTS="%{rpmcflags} -Wall -I/usr/X11R6/include" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README HINTS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmapm.desktop
