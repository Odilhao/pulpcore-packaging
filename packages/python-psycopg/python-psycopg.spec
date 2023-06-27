%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name psycopg

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.1.9
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python

License:        GNU Lesser General Public License v3 (LGPLv3)
URL:            https://psycopg.org/psycopg3/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-black >= 23.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-dnspython >= 2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8 >= 4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy >= 1.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-types-setuptools >= 57.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel >= 0.37


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Sphinx >= 5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-anyio >= 3.6.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-backports-zoneinfo >= 0.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-furo = 2022.6.21
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy >= 1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pproxy >= 2.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg-binary = 3.1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg-c = 3.1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg-pool
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.2.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov >= 3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-randomly >= 3.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-autobuild >= 2021.3.14
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-autodoc-typehints >= 1.12
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions >= 4.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-tzdata


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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 27 2023 Odilon Sousa - 3.1.9-1
- Initial package.
