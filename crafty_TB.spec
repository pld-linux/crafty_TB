Summary:	Tablebases for Crafty
Summary(pl):	Bazy danych dla Crafty
Name:		crafty_TB
Version:	2.0
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.cis.uab.edu/pub/hyatt/TB/31/kbnk.nbb.emd
# Source0-md5:	891e2e92ec49c72973a6456e71b02459
Source1:	ftp://ftp.cis.uab.edu/pub/hyatt/TB/31/kbnk.nbw.emd
# Source1-md5:	19d67aeba1329762a5a076917b5b7f61
Icon:		xchess.gif
Requires:	crafty
Obsoletes:	crafty_tablebase
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selected endgame tablebases for Crafty.

%description -l pl
Baza danych wybranych zakoñczeñ gry dla Crafty.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/games/crafty/TB

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/games/crafty/TB

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/games/crafty/TB
%{_libdir}/games/crafty/TB/kbnk.nbb.emd
%{_libdir}/games/crafty/TB/kbnk.nbw.emd
