%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name asgiref

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.7.2
Release:        1%{?dist}
Summary:        ASGI specs, helper code, and adapters

License:        BSD-3-Clause
URL:            https://github.com/django/asgiref/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.800
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 4


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.800
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-asyncio
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 4


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 3.7.2-1
- Update to 3.7.2

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 3.6.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 3.6.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 3.6.0-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 3.6.0-1
- Update to 3.6.0

* Tue Sep 20 2022 Odilon Sousa 3.5.2-1
- Update to 3.5.2

* Tue Apr 26 2022 Yanis Guenane - 3.5.0-2
- Build against Python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 3.5.0-1
- Release python-asgiref 3.5.0

* Wed Sep 08 2021 Evgeni Golov - 3.4.1-1
- Initial package.
