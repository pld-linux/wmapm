Summary:	Dockable APM/Battery Monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM dla WindowMakera
Summary(pt_BR):	Aplicativo do dock do WindowMaker para monitorar a carga da bateria
Summary(es):	Una aplicación para monitorar la batería en el dock del WindowMaker
Name:		wmapm
Version:	3.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
Linuksa. WMAPM dostarcza obecnie nastêpuj±cych informacji:
	* Rodzaj wykorzystywanego ¼ród³a energii (bateria lub zasilacz);
	* D³ugo¶æ ¿ycia baterii (w procentach lub graficznie);
	* Czas pozosta³y do wyczerpania baterii;
	* Stan obci±¿enia baterii;
	* Stan baterii: Wysoki/Niski/Krytyczny (Czerwony/¯ó³ty/Zielony);
	
%description -l pt_BR
Aplicativo do dock do WindowMaker para monitorar a carga da bateria,
através do suporte APM do kernel. Esta informação é útil para
usuários de laptops.

%description -l es
Aplicación para monitorar la batería en el dock del WindowMaker.
Basado en soporte APM del kernel. Es útil en notebooks.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
	COPTS="%{rpmcflags} -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README HINTS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
#%{_applnkdir}/DockApplets/wmapm.desktop
