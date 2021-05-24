#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-OpenID-Consumer
Version  : 1.18
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Consumer-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Consumer-1.18.tar.gz
Summary  : 'Library for consumers of OpenID identities'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-OpenID-Consumer-license = %{version}-%{release}
Requires: perl-Net-OpenID-Consumer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(CGI)
BuildRequires : perl(Crypt::DH::GMP)
BuildRequires : perl(HTML::Parser)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(JSON)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Net::OpenID::Common)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(XML::Simple)

%description
Net-OpenID-Consumer
===================
This is a set of Perl modules for implementing
a Relying Party for OpenID (versions 1.1 or 2.0)

%package dev
Summary: dev components for the perl-Net-OpenID-Consumer package.
Group: Development
Provides: perl-Net-OpenID-Consumer-devel = %{version}-%{release}
Requires: perl-Net-OpenID-Consumer = %{version}-%{release}

%description dev
dev components for the perl-Net-OpenID-Consumer package.


%package license
Summary: license components for the perl-Net-OpenID-Consumer package.
Group: Default

%description license
license components for the perl-Net-OpenID-Consumer package.


%package perl
Summary: perl components for the perl-Net-OpenID-Consumer package.
Group: Default
Requires: perl-Net-OpenID-Consumer = %{version}-%{release}

%description perl
perl components for the perl-Net-OpenID-Consumer package.


%prep
%setup -q -n Net-OpenID-Consumer-1.18
cd %{_builddir}/Net-OpenID-Consumer-1.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-OpenID-Consumer
cp %{_builddir}/Net-OpenID-Consumer-1.18/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-OpenID-Consumer/fa7342adb982b2bc5de778c2a7124d6389d05c1a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::OpenID::Association.3
/usr/share/man/man3/Net::OpenID::ClaimedIdentity.3
/usr/share/man/man3/Net::OpenID::Consumer.3
/usr/share/man/man3/Net::OpenID::VerifiedIdentity.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-OpenID-Consumer/fa7342adb982b2bc5de778c2a7124d6389d05c1a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Net/OpenID/Association.pm
/usr/lib/perl5/vendor_perl/5.32.1/Net/OpenID/ClaimedIdentity.pm
/usr/lib/perl5/vendor_perl/5.32.1/Net/OpenID/Consumer.pm
/usr/lib/perl5/vendor_perl/5.32.1/Net/OpenID/VerifiedIdentity.pm
