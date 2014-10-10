%define upstream_name    HTML-TreeBuilder-XPath
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.14
Release:	2

Summary:	Add XPath support to HTML::TreeBuilder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-TreeBuilder-XPath-0.14.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(XML::XPathEngine)
# Some of these requirements were missing so we added them explicitly.
Requires:	perl(List::Util)
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(HTML::TreeBuilder::XPath::Node)
Requires:	perl(Scalar::Util)
Requires:	perl(XML::XPathEngine)

BuildArch:	noarch

%description
This module adds typical XPath methods to HTML::TreeBuilder, to make it
easy to query a document.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.120.0-3mdv2011.0
+ Revision: 654348
- rebuild for updated spec-helper

* Sat Dec 04 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 609572
- Specified the Requires explicitly

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 607286
- import perl-HTML-TreeBuilder-XPath


