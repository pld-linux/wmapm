Summary:	Dockable APM/Battery Monitor for WindowMaker
Summary(pl):	Dokowalny monitor APM dla WindowMakera
Name:		wmapm
Version: 	3.01
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

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
cd wmapm
make clean
make COPTS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/man/man1}

install -s wmapm/wmapm $RPM_BUILD_ROOT/usr/X11R6/bin
install wmapm/wmapm.1 $RPM_BUILD_ROOT/usr/X11R6/share/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	BUGS CHANGES README HINTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README,HINTS,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/wmapm

/usr/X11R6/share/man/man1/wmapm.1.gz

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.01-1]
- now package is FHS 2.0 compliant.

* Wed Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
- initial rpm release for PLD.
