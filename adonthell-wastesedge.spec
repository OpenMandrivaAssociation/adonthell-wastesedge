%define	mname	adonthell
%define	rname	wastesedge
%define	name	%{mname}-%{rname}

Name:		%{name}
Summary:	Role-playing game (RPG)
Version:	0.3.4
Release:	%mkrel 3
License:	GPL+
Group:		Games/Adventure
Source0:	http://freesoftware.fsf.org/download/adonthell/%{rname}-src-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
URL:		http://adonthell.linuxgames.com/
BuildArch:	noarch
Requires:	%{mname} >= %{version}
BuildRequires:	%{mname} >= %{version}
BuildRequires:	python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
As a loyal servant of the elven Lady Silverhair, you arrive at the remote
trading post of Waste's Edge, where she is engaged in negotiations with the
dwarish merchant Bjarn Fingolson. But not all is well at Waste's Edge, and
soon you are confronted with circumstances that are about to destroy your
mistress' high reputation. And you are the only one to avert this...

%prep
%setup -q -n %{rname}-%{version}

%build
./configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}/%{mname}/games/%{rname} \
		--with-adonthell-binary=%{_gamesbindir}/%{mname}

%make

%install
rm -rf %{buildroot}
%{makeinstall_std} datadir=%{_datadir}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;AdventureGame;
Name=Adonthell - Waste's Edge
Comment=Open source role-playing game
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{rname}

%post
%{update_menus}
%{update_icon_cache hicolor}

%postun
%{clean_menus}
%{clean_icon_cache hicolor}

%clean
rm -rf %{buildroot}

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS PLAYING README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{mname}/games/%{rname}
%{_datadir}/pixmaps/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

