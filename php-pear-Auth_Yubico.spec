%define		status		alpha
%define		pearname	Auth_Yubico
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Authentication class for verifying Yubico OTP tokens
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

%define		_sysconfdir	%(pear config-get cfg_dir 2>/dev/null || ERROR)/%{pearname}

%description
PHP class to help you verify Yubico OTP tokens.

In PEAR status of this package is: %{status}.

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

%if 0%{?_noautoreq:1}
%post -p <lua>
%pear_package_print_optionalpackages
%endif

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%if 0%{?_noautoreq:1}
%doc optional-packages.txt
%endif
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Auth/Yubico.php



