%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Rc4
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Encryption class for RC4 encryption
Summary(pl):	%{_class}_%{_subclass} - Klasa szyfruj±ca w algorytmie RC4
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RC4 encryption class.

%description -l pl
Klasa szyfruj±ca w algorytmie RC4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
