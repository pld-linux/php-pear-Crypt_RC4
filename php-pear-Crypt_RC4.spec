%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Rc4
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Encryption class for RC4 encryption
Summary(pl):	%{_pearname} - Klasa szyfrująca w algorytmie RC4
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	90837b9317deaf42f563958b4689b937
URL:		http://pear.php.net/package/Crypt_Rc4/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RC4 encryption class.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa szyfrująca w algorytmie RC4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_class}_RC4-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
