%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name is-windows

Summary:       Returns true if the platform is windows
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.0
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-windows
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Returns true if the platform is windows.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Dec 02 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-3
- Enbale scl macros

* Tue Nov 24 2015 Troy Dawson <tdawson@redhat.com> - 0.1.0-1
- Initial package
