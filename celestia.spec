Summary:	A real-time visual space simulation
Summary(pl):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/celestia/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.shatters.net/celestia/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	glut-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	OpenGL-devel
Requires:	OpenGL
Requires:	%{name}-extrasolar
Requires:	%{name}-deepsky
Requires:	%{name}-stars
Requires:	%{name}-textures-mercury
Requires:	%{name}-textures-earth
Requires:	%{name}-textures-earth-clouds
Requires:	%{name}-textures-earth-night
Requires:	%{name}-textures-moon
Requires:	%{name}-textures-mars
Requires:	%{name}-textures-jupiter
Requires:	%{name}-textures-galileanmoons
Requires:	%{name}-textures-saturn
Requires:	%{name}-textures-triton
Requires:	%{name}-textures-pluto
Obsoletes:	%{name}-textures-stars
Obsoletes:	%{name}-asterisms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Celestia is a free real-time space simulation that lets you experience
our universe in three dimensions. Unlike most planetarium software,
Celestia doesn't confine you to the surface of the Earth. You can
travel throughout the solar system, to any of over 100,000 stars, or
even beyond the galaxy. All travel in Celestia is seamless; the
exponential zoom feature lets you explore space across a huge range of
scales, from galaxy clusters down to spacecraft only a few meters
across. A 'point-and-goto' interface makes it simple to navigate
through the universe to the object you want to visit.

%description -l pl
Celestia to wolny symulator przestrzeni komicznej w czasie
rzeczywistym, kt�ry pozwala do�wiadcza� naszego Wszech�wiata w trzech
wymiarach. W odr�nieniu od innych program�w planetarnych Celestia nie
przywi�zuje Ci� do powierzchni ziemi. Mo�esz podr�owa� przez Uk�ad
S�oneczny do ponad 100,000 gwiazd lub nawet poza galaktyk�. Wszystkie
podr�e w Celestii s� niezauwa�alne; funkcja wyk�adniczego
przybli�enia pozwala Ci odkrywa� Kosmos w r�nych skalach - od
spojrzenia na galaktyki do widoku kilkumetrowych statk�w kosmicznych.
Interfejs typu 'poka�-i-le�' czyni nawigacj� przez Wszech�wiat prost�.

%package task-default
Summary:	Default packages for celestia
Summary(pl):	Domy�lne pakiety dla celestii
Group:		X11/Applications/Science
Requires:	%{name}-extrasolar-default
Requires:	%{name}-deepsky-default
Requires:	%{name}-stars-default
Requires:	%{name}-textures-mercury-default
Requires:	%{name}-textures-earth-default
Requires:	%{name}-textures-earth-clouds-default
Requires:	%{name}-textures-earth-night-default
Requires:	%{name}-textures-moon-default
Requires:	%{name}-textures-mars-default
Requires:	%{name}-textures-jupiter-default
Requires:	%{name}-textures-galileanmoons-default
Requires:	%{name}-textures-saturn-default
Requires:	%{name}-textures-triton-default
Requires:	%{name}-textures-pluto-default

%description task-default
Default packages for celestia. This metapackage contains no files
and can be safely uninstalled after installation.

%description task-default -l pl
Domy�lne pakiety dla celestii. Ten metapakiet nie zawiera �adnych
plik�w i mo�e zosta� usuni�ty po instalacji.

%package extrasolar-default
Summary:	Catalog of known extrasolar planetary systems
Summary(pl):	Katalog znanych uk�ad�w planetarnych
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-extrasolar
Obsoletes:	%{name}-extrasolar

%description extrasolar-default
Catalog of known extrasolar planetary systems.

%description extrasolar-default -l pl
Katalog znanych uk�ad�w planetarnych.

%package deepsky-default
Summary:	Galaxy catalog (8 galaxies)
Summary(pl):	Katalog o�miu galaktyk
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-deepsky
Obsoletes:	%{name}-deepsky
Obsoletes:	%{name}-galaxies

%description deepsky-default
Galaxy catalog (8 galaxies).

%description deepsky-default -l pl
Katalog o�miu galaktyk.

%package stars-default
Summary:	Database with 100 000 stars
Summary(pl):	Baza danych 100 000 gwiazd
Group:		X11/Applications/Science
Requires:	%{name}
Provides:	%{name}-stars
Obsoletes:	%{name}-stars

%description stars-default
Initial Stars database (with about 100 000 Hipparcos stars).

%description stars-default -l pl
Podstawowa baza danych gwiazd (z oko�o 100 000 gwiazd zbadanych
przez sond� kosmiczn� Hipparcos).

%package textures-mercury-default
Summary:	1k Mercury textures
Summary(pl):	Tekstury Merkurego o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-mercury
Obsoletes:	%{name}-textures-mercury

%description textures-mercury-default
1k Mercury textures.

%description textures-mercury-default -l pl
Tekstury Merkurego o wielko�ci 1024 x 512.

%package textures-earth-default
Summary:	2k Earth textures
Summary(pl):	Tekstury Ziemi o wielko�ci 2048 x 1024
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-earth
Obsoletes:	%{name}-textures-earth

%description textures-earth-default
2k Earth textures.

%description textures-earth-default -l pl
Tekstury Ziemi o wielko�ci 2048 x 1024.

%package textures-earth-clouds-default
Summary:	1k Earth cloud textures
Summary(pl):	Tekstury ziemskich chmur o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-earth-clouds
Obsoletes:	%{name}-textures-earth-clouds

%description textures-earth-clouds-default
1k Earth clouds textures.

%description textures-earth-clouds-default -l pl
Tekstury ziemskich chmur o wielko�ci 1024 x 512.

%package textures-earth-night-default
Summary:	1k Earth night textures
Summary(pl):	Tekstury nocnych �wiate� miast o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-earth-night
Obsoletes:	%{name}-textures-earth-night

%description textures-earth-night-default
1k Earth night textures.

%description textures-earth-night-default -l pl
Tekstury nocnych �wiate� miast o wielko�ci 1024 x 512.

%package textures-moon-default
Summary:	1k Moon textures
Summary(pl):	Tekstury Ksi�yca o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-moon
Obsoletes:	%{name}-textures-moon

%description textures-moon-default
1k Moon textures.

%description textures-moon-default -l pl
Tekstury Ksi�yca o wielko�ci 1024 x 512.

%package textures-mars-default
Summary:	1k Mars textures
Summary(pl):	Tekstury Marsa o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-mars
Obsoletes:	%{name}-textures-mars

%description textures-mars-default
1k Mars textures.

%description textures-mars-default -l pl
Tekstury Marsa o wielko�ci 1024 x 512.

%package textures-jupiter-default
Summary:	1k Jupiter textures
Summary(pl):	Tekstury Jowisza o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-jupiter
Obsoletes:	%{name}-textures-jupiter

%description textures-jupiter-default
1k Jupiter textures.

%description textures-jupiter-default -l pl
Tekstury Jowisza o wielko�ci 1024 x 512.

%package textures-galileanmoons-default
Summary:	1k galilean moons textures
Summary(pl):	Tekstury ksi�yc�w odkrytych przez Galileusza o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-galileanmoons
Obsoletes:	%{name}-textures-galileanmoons

%description textures-galileanmoons-default
1k galilean moons (Io, Europa, Ganymede, Calypso) textures.

%description textures-galileanmoons-default -l pl
Tekstury ksi�yc�w Jowisza odkrytych przez Galileusza (Io,
Europa, Ganimedes, Calypso) o wielko�ci 1024 x 512.

%package textures-saturn-default
Summary:	256 Saturn textures
Summary(pl):	Tekstury Saturna o wielko�ci 256 x 128
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-saturn
Obsoletes:	%{name}-textures-saturn

%description textures-saturn-default
256 Saturn textures.

%description textures-saturn-default -l pl
Tekstury Jowisza o wielko�ci 256 x 128.

%package textures-triton-default
Summary:	512 Triton textures
Summary(pl):	Tekstury Trytona o wielko�ci 512 x 256
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-triton
Obsoletes:	%{name}-textures-triton

%description textures-triton-default
512 Triton textures.

%description textures-triton-default -l pl
Tekstury najwi�kszego ksi�yca Neptuna, Trytona
o wielko�ci 512 x 256.

%package textures-pluto-default
Summary:	1k Pluto textures
Summary(pl):	Tekstury Plutona o wielko�ci 1024 x 512
Group:		X11/Applications/Science
Prereq:		%{name}
Provides:	%{name}-textures-pluto
Obsoletes:	%{name}-textures-pluto

%description textures-pluto-default
1k Pluto textures.

%description textures-pluto-default -l pl
Tekstury Plutona o wielko�ci 1024 x 512.

%prep
%setup -q

echo "You can remove this package safely." > PLACEHOLDER-TASK-DEFAULT

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--disable-rpath \
	--with-kde \
	--without-gtk \
	--without-lua \
	--with-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Scientific/Astronomy}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# desktop/icon
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Astronomy/%{name}.desktop
cp src/celestia/kde/data/hi48-app-celestia.png $RPM_BUILD_ROOT%{_pixmapsdir}/celestia.png

# solarsys.ssc generator
mkdir $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/data/solarsys
cat > $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/solarsys-gen << EOF
#!/bin/sh
cd %{_datadir}/apps/%{name}/data
LANG=C cat solarsys/* > solarsys.ssc
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO controls.txt ChangeLog
%doc %{_datadir}/apps/celestia/manual
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/apps/celestia/solarsys-gen
%dir %{_datadir}/apps/celestia
%dir %{_datadir}/apps/celestia/data
%{_datadir}/apps/celestia/data/asterisms.dat
%{_datadir}/apps/celestia/data/boundaries.dat
%{_datadir}/apps/celestia/data/galileo.xyz
%verify(not md5 size mtime) %{_datadir}/apps/celestia/data/solarsys.ssc
%{_datadir}/apps/celestia/data/hdnames.dat
%{_datadir}/apps/celestia/data/starnames.dat
%{_datadir}/apps/celestia/extras
%{_datadir}/apps/celestia/favicons
%{_datadir}/apps/celestia/fonts
%{_datadir}/apps/celestia/models
%{_datadir}/apps/celestia/shaders
%dir %{_datadir}/apps/celestia/textures
%{_datadir}/apps/celestia/textures/lores
%{_datadir}/apps/celestia/textures/medres
%exclude %{_datadir}/apps/celestia/textures/medres/callisto.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/earth*
%exclude %{_datadir}/apps/celestia/textures/medres/europa.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/ganymede.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/io.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/jupiter.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/mars*
%exclude %{_datadir}/apps/celestia/textures/medres/mercury*
%exclude %{_datadir}/apps/celestia/textures/medres/moon*
%exclude %{_datadir}/apps/celestia/textures/medres/pluto*
%exclude %{_datadir}/apps/celestia/textures/medres/saturn*
%exclude %{_datadir}/apps/celestia/textures/medres/triton*
%exclude %{_datadir}/apps/celestia/textures/medres/venus.jpg
%exclude %{_datadir}/apps/celestia/textures/medres/venussurface.jpg
%{_datadir}/apps/celestia/textures/flare.jpg
%{_datadir}/apps/celestia/textures/logo.png
%{_datadir}/apps/celestia/bookmarks.xml
%{_datadir}/apps/celestia/celestia.cfg
%{_datadir}/apps/celestia/celestiaui.rc
%{_datadir}/apps/celestia/controls.txt
%{_datadir}/apps/celestia/*.cel

%{_applnkdir}/Scientific/Astronomy/*
%{_pixmapsdir}/*
%{_datadir}/config
%{_datadir}/doc/HTML/en/%{name}
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*

%files task-default
%defattr(644,root,root,755)
%doc PLACEHOLDER-TASK-DEFAULT

%files extrasolar-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/data/extrasolar.ssc

%files deepsky-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/data/deepsky.dsc

%files stars-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/data/stars.dat

%files textures-mercury-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/mercury.jpg
%{_datadir}/apps/celestia/textures/medres/mercurybump.jpg

%files textures-earth-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earth.png

%files textures-earth-clouds-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earth-clouds.png

%files textures-earth-night-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/earthnight.jpg

%files textures-moon-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/moon.jpg
%{_datadir}/apps/celestia/textures/medres/moonbump1k.jpg

%files textures-mars-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/mars.jpg
%{_datadir}/apps/celestia/textures/medres/marsbump1k.jpg

%files textures-jupiter-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/jupiter.jpg

%files textures-galileanmoons-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/callisto.jpg
%{_datadir}/apps/celestia/textures/medres/io.jpg
%{_datadir}/apps/celestia/textures/medres/europa.jpg
%{_datadir}/apps/celestia/textures/medres/ganymede.jpg

%files textures-saturn-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/saturn.jpg

%files textures-triton-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/triton.jpg

%files textures-pluto-default
%defattr(644,root,root,755)
%{_datadir}/apps/celestia/textures/medres/pluto.jpg
%{_datadir}/apps/celestia/textures/medres/plutobump1k.jpg
