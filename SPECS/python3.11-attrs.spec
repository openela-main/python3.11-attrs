%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global modname attrs

%if 0%{?rhel} && 0%{?rhel} <= 9
# Can't run tests on RHEL9 due to the need for hypothesis and zope-interface
%bcond_with tests
%else
# Turn the tests off when bootstrapping Python, because pytest requires attrs
%bcond_without tests
%endif

Name:           python%{python3_pkgversion}-attrs
Version:        22.1.0
Release:        1%{?dist}
Summary:        Python attributes without boilerplate

License:        MIT
URL:            http://www.attrs.org/
BuildArch:      noarch
Source0:        https://github.com/hynek/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-hypothesis
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-zope-interface
%endif


%description -n python%{python3_pkgversion}-%{modname}
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%prep
%setup -q -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} py.test-%{python3_pkgversion} -v
%endif

%files
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/*

%changelog
* Wed Oct 19 2022 Charalampos Stratakis <cstratak@redhat.com> - 22.1.0-1
- Initial package
- Fedora contributions by:
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Tomas Hrnciar <thrnciar@redhat.com>
