%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Rc4
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Encryption class for RC4 encryption
Summary(pl):	%{_pearname} - Klasa szyfruj±ca w algorytmie RC4
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cf041f0b6250af8bf8fe48e3c2658ed5
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RC4 encryption class.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa szyfruj±ca w algorytmie RC4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
