Summary:	Bonus map pack for Warmux
Summary(pl.UTF-8):	Dodatkowy zestaw map dla gry Warmux
Name:		warmux-bonusmaps
Version:	20100501
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.gna.org/warmux/Wormux-BonusMaps-%{version}.tar.gz
# Source0-md5:	c6c969dbe3dabdef95fb3a99bb6bbeda
URL:		http://www.warmux.org/
Requires:	warmux >= 11.01
Obsoletes:	wormux-bonusmaps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonus map pack for Warmux.

%description -l pl.UTF-8
Dodatkowy zestaw map dla gry Warmux.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/warmux/map

# included in main warmux game
%{__rm} -r urbanheights

find -maxdepth 1 -mindepth 1 -type d -print0 -exec sh -c 'cp -rf "{}" $RPM_BUILD_ROOT%{_datadir}/games/warmux/map' \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/warmux/map
