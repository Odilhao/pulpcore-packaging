%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name zipp

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.7.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        None
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-func-timeout
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jaraco-itertools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jaraco-packaging >= 8.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-black >= 0.3.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-checkdocs >= 2.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-enabler >= 1.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-flake8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rst-linker >= 1.9
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-func-timeout
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jaraco-itertools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jaraco-packaging >= 8.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-black >= 0.3.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-checkdocs >= 2.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-enabler >= 1.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-flake8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-rst-linker >= 1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx


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
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 3.7.0-1
- Update to 3.7.0

* Mon Sep 06 2021 Evgeni Golov - 3.4.0-3
- Build against Python 3.8

* Thu Nov 05 2020 Evgeni Golov - 3.4.0-2
- Fix License tag in spec file

* Thu Oct 29 2020 Evgeni Golov 3.4.0-1
- Update to 3.4.0

* Thu Jun 04 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 2.1.0-1
- Initial package.
