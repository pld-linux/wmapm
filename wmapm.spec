Summary:	Dockable APM/Battery Monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM dla WindowMakera
Name:		wmapm
Version: 	3.01
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	wmapm.desktop
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
WMAPM monitors the APM statistics through the APM support in
the Linux kernel. WMAPM currently provides:
        * Status of power supply (battery or AC);
        * Percentage of battery remaining (numeric and meter);
        * Battery charging status;
        * Time left to battery depletion;
        * High/Low/Critical battery status (Red/Yellow/Green);

%description -l pl
WMAPM monitoruje statystyki APM wykorzystuj�c funkcje zawarte w j�drze
Linuxa. WMAPM dostarcza obecnie nast�puj�cych informacji:
	* Rodzaj wykorzystywanego �r�d�a energii (bateria lub zasilacz);
	* D�ugo�� �ycia baterii (w procentach lub graficznie);
	* Czas pozosta�y do wyczerpania baterii;
	* Stan obci��enia baterii;
	* Stan baterii: Wysoki/Niski/Krytyczny (Czerwony/��ty/Zielony);

%prep
%setup -q

%build
make -C %{name} clean
make -C %{name} \
	COPTS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/applnk/DockApplets 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS CHANGES README HINTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README,HINTS,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

/etc/X11/applnk/DockApplets/wmapm.desktop

%changelog
* Sun May  9 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.01-1]
- now package is FHS 2.0 compliant.

* Wed Apr  5 1999 Piotr Czerwi�ski <pius@pld.org.pl>
- initial rpm release for PLD.
