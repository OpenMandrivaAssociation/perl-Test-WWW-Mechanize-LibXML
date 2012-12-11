%define upstream_name    Test-WWW-Mechanize-LibXML
%define upstream_version v0.0.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Use HTML::TreeBuilder::LibXML for testing
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.xz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::TreeBuilder::LibXML)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(MRO::Compat)
BuildArch:	noarch

%description
This module inherits from the Test::WWW::Mechanize manpage, and allows one
to utilize the HTML::TreeBuilder::LibXML manpage to perform XPath and the
HTML::TreeBuilder manpage queries on the tree.

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
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 657848
- rebuild for updated spec-helper

* Tue Dec 07 2010 Shlomi Fish <shlomif@mandriva.org> 0.0.2-2mdv2011.0
+ Revision: 614461
- Add a missing dep - MRO::Compat
- import perl-Test-WWW-Mechanize-LibXML

