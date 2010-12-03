%define upstream_name    Test-WWW-Mechanize-LibXML
%define upstream_version v0.0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Use HTML::TreeBuilder::LibXML for testing
License:    MIT
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.xz

BuildRequires: perl(HTML::TreeBuilder::LibXML)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module inherits from the Test::WWW::Mechanize manpage, and allows one
to utilize the HTML::TreeBuilder::LibXML manpage to perform XPath and the
HTML::TreeBuilder manpage queries on the tree.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


