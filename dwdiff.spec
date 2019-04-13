Summary:	diff frontend that operates on words
Summary(pl.UTF-8):	frontend do diffa operujący na słowach
Name:		dwdiff
Version:	2.1.2
Release:	2
License:	GPL v3
Group:		Applications/Text
Source0:	http://os.ghalkes.nl/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	4ff3c3851170dcd6243870af5ecb5b68
URL:		http://os.ghalkes.nl/dwdiff.html
BuildRequires:	gettext-tools
BuildRequires:	libicu-devel
BuildRequires:	pkgconfig
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dwdiff is a front-end for the diff program that operates at the word
level instead of the line level. It is different from wdiff in that it
allows the user to specify what should be considered whitespace, and
in that it takes an optional list of characters that should be
considered delimiters. Delimiters are single characters that are
treated as if they are words, even when there is no whitespace
separating them from preceding words or delimiters. dwdiff is mostly
commandline compatible with wdiff. Only the --autopager, --terminal
and --avoid-wraps options are not supported.

The default output from dwdiff is the new text, with the deleted and
inserted parts annotated with markers. Command line options are
available to change both what is printed, and the markers.

%description -l pl.UTF-8
dwdiff to frontend do programu diff operujący na słowach zamiast na
liniach. W odróżnieniu od wdiff pozwala użytkownikowi na określenie co
traktować jako biały znak oraz ustalenie listy delimetrów. Delimeter
to pojedynczy znak traktowany jak słowo nawet jeśli nie ma białych
znaków oddzielających go od innych słów czy delimetrów. dwdiff jest w
dużej mierze kompatybilny z wdiff, jedynie opcje --autopager,
 --terminal i --avoid-wraps nie są wspierane.

Domyślnym formatem wyjściowym dwdiff jest nowy tekst z częściami
usuniętymi i dodanymi oznaczonymi markerami. Z poziomu linii poleceń
możliwe jest określenie co i za pomocą jakich znaczników ma być
wyświetlane.

%prep
%setup -q

%build
# not a typical configure
./configure \
	--prefix="$RPM_BUILD_ROOT%{_prefix}" \
	--mandir="$RPM_BUILD_ROOT%{_mandir}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install

%find_lang %{name}

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/dw*.1*
%lang(nl) %{_mandir}/nl/man1/dw*.1*
