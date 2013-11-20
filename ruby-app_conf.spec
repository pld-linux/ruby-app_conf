%define	pkgname	app_conf
Summary:	Simplest YAML Backed Application Wide Configuration
Name:		ruby-%{pkgname}
Version:	0.4.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	fc0f790c06355c87ac2717eaa16ca605
URL:		https://github.com/PhilT/app_conf
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML Backed Application Wide Configuration with a few extras
(AppConfig like)

- Supports nested key/values
- Loading and Saving of YAML files
- Add further key/value pairs in code
- Use dot or bracket notation
- AppConf#to_hash outputs a hash map of AppConf key/values
- AppConf#from_hash creates nested key/values from a hash

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown LICENSE 
%{ruby_vendorlibdir}/%{pkgname}.rb
