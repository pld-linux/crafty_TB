Name:		crafty_tablebase
Requires:	crafty
Version:	2.0
Summary:	Tablebases for Crafty.
Release:	3
ExcludeArch:	axp
License:	GPL
Group:		Applications/Games
Icon:		xchess.gif
Source0:	ftp://ftp.cis.uab.edu/pub/hyatt/TB/four/kbnk.nbb.emd
Source1:	ftp://ftp.cis.uab.edu/pub/hyatt/TB/four/kbnk.nbw.emd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selected endgame tablebases for Crafty.

%prep
echo Nothing to do for prep.

%build
echo Nothing to do for build.

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/lib/games/crafty/TB
install -m 0444 ${RPM_SOURCE_DIR}/kbnk.nbb.emd $RPM_BUILD_ROOT%{_prefix}/lib/games/crafty/TB
install -m 0444 ${RPM_SOURCE_DIR}/kbnk.nbw.emd $RPM_BUILD_ROOT%{_prefix}/lib/games/crafty/TB

%files
%defattr(644,root,root,755)
%dir %{_prefix}/lib/games/crafty/TB
%{_prefix}/lib/games/crafty/TB/kbnk.nbb.emd
%{_prefix}/lib/games/crafty/TB/kbnk.nbw.emd