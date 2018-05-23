%define		status		alpha
%define		pearname	Auth_Yubico
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Authentication class for verifying Yubico OTP tokens
Summary(pl.UTF-8):	%{pearname} - klasa uwierzytelniająca do weryfikowania tokenów OTP Yubico
Name:		php-pear-Auth_Yubico
Version:	2.5
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://developers.yubico.com/php-yubico/Releases/Auth_Yubico-%{version}.tgz
# Source0-md5:	955f8330a5e030904394c6892d09a4c4
URL:		https://developers.yubico.com/php-yubico/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP class to help you verify Yubico OTP tokens.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa PHP pomagająca weryfikować tokeny OTP Yubico.

Ta klasa ma w PEAR status: %{status}.

%prep
%setup -q -n Auth_Yubico-%{version}
%define builddir $(pwd)
%pear_install
cat .install.log | %__pear_install_log
%undos -f php,html,js,xml

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/auth_yubico.reg
%{php_pear_dir}/Auth/Yubico.php
