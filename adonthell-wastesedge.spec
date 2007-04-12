%define	mname	adonthell
%define	rname	wastesedge
%define	name	%{mname}-%{rname}
%define version	0.3.4
%define release	1mdk
%define	Summary	Official game package for Adonthell

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Adventure
Source0:	http://freesoftware.fsf.org/download/adonthell/%{rname}-src-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
URL:		http://adonthell.linuxgames.com/
BuildArch:	noarch
Requires:	%{mname} >= %{version}
BuildRequires:	%{mname} >= %{version}
Summary:	%{Summary}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
As a loyal servant of the elven Lady Silverhair, you arrive at the remote
trading post of Waste's Edge, where she is engaged in negotiations with the
dwarish merchant Bjarn Fingolson. But not all is well at Waste's Edge, and
soon you are confronted with circumstances that are about to destroy your
mistress' high reputation. And you are the only one to avert this ...

%prep
%setup -q -n %{rname}-%{version}

%build
./configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}/%{mname}/games/%{rname} \
		--with-adonthell-binary=%{_gamesbindir}/%{mname}

%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} datadir=%{_datadir}
#ROOT%{_gamesbindir} gamedatadir=$RPM_BUILD_ROOT%{_gamesdatadir}/%{mname}/games/%{rname}

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF >$RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon=%{name}.png \
		  needs="x11" \
		  section="More Applications/Games/Adventure" \
		  title="Adonthell - Waste's Edge"\
		  longtitle="%{Summary}"
EOF

install -m644 %{SOURCE11} -D ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

%find_lang %{rname}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS PLAYING README
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{mname}/games/%{rname}
%{_gamesdatadir}/%{mname}/games/%{rname}/*
%{_datadir}/pixmaps/*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png

