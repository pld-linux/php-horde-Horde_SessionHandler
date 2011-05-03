%define		status		stable
%define		pearname	Horde_SessionHandler
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Session Handler API
Name:		php-horde-Horde_SessionHandler
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	f9fe35cd2d47e09636892ddf5a2c7abf
URL:		https://github.com/horde/horde/tree/master/framework/SessionHandler/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Log
Suggests:	php-horde-Horde_Memcache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Db.*) pear(Horde/Log.*) pear(Horde/Memcache.*)

%description
Horde_SessionHandler defines an API for implementing custom session
handlers for PHP.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/SessionHandler.php
%{php_pear_dir}/Horde/SessionHandler
%{php_pear_dir}/data/Horde_SessionHandler
