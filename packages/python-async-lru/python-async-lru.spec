%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name async-lru

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.0.4
Release:        1%{?dist}
Summary:        Simple LRU cache for asyncio

License:        MIT License
URL:            https://github.com/aio-libs/async-lru
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 4.0.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 4.0.0


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
%{python3_sitelib}/async_lru
%{python3_sitelib}/async_lru-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 2.0.4-1
- Update to 2.0.4

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.0.3-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.3-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 1.0.3-1
- Update to 1.0.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.0.2-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 1.0.2-2
- Build against Python 3.8

* Mon Jan 11 2021 Evgeni Golov - 1.0.2-1
- Initial package.
