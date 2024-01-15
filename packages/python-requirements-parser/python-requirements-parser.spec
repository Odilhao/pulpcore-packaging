%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name requirements-parser

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        This is a small Python module for parsing Pip requirement files

License:        None
URL:            https://github.com/madpah/requirements-parser
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-types-setuptools >= 57.0.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/requirements
%{python3_sitelib}/requirements_parser-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 0.5.0-1
- Update to 0.5.0

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.2.0-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.2.0-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.2.0-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.2.0-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.2.0-2
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 0.2.0-1
- Initial package.
