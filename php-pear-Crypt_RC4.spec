%define		_status		stable
%define		_pearname	Crypt_RC4
Summary:	%{_pearname} - Encryption class for RC4 encryption
Summary(pl.UTF-8):	%{_pearname} - Klasa szyfrująca w algorytmie RC4
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	571483de3a74b74f49c25e49ace04d89
URL:		http://pear.php.net/package/Crypt_RC4/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Crypt_Rc4 < 1.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RC4 encryption class.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa szyfrująca w algorytmie RC4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/*.php
