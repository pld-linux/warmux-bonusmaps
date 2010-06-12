Summary:	Bonus map pack for Wormux
Summary(pl.UTF-8):	Dodatkowy zestaw map dla gry Wormux
Name:		wormux-bonusmaps
Version:	20100501
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.gna.org/wormux/Wormux-BonusMaps-%{version}.tar.gz
# Source0-md5:	c6c969dbe3dabdef95fb3a99bb6bbeda
URL:		http://www.wormux.org/
Requires:	wormux >= 0.9.2.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonus map pack for Wormux.

%description -l pl.UTF-8
Dodatkowy zestaw map dla gry Wormux.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/wormux/map

find -maxdepth 1 -mindepth 1 -type d -print0 -exec sh -c 'cp -rf "{}" $RPM_BUILD_ROOT%{_datadir}/games/wormux/map' \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/wormux/map
