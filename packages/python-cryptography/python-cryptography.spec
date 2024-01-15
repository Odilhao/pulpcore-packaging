%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        41.0.4
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        Apache-2.0 OR BSD-3-Clause
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bcrypt >= 3.1.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-black
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-build
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-check-sdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-nox
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pretend
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyenchant >= 1.6.11
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-benchmark
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-randomly
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ruff
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-twine >= 1.12.0


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bcrypt >= 3.1.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-black
Requires:       %{?scl_prefix}python%{python3_pkgversion}-build
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cffi >= 1.12
Requires:       %{?scl_prefix}python%{python3_pkgversion}-check-sdist
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy
Requires:       %{?scl_prefix}python%{python3_pkgversion}-nox
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pretend
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyenchant >= 1.6.11
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-benchmark
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-randomly
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ruff
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx >= 5.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-rtd-theme >= 1.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinxcontrib-spelling >= 4.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-twine >= 1.12.0


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
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 41.0.4-1
- Update to 41.0.4

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 38.0.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 38.0.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-2
- Build against python 3.11

* Wed Jan 25 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-1
- Release python-cryptography 38.0.4

* Tue Apr 26 2022 Odilon Sousa <osousa@redhat.com> - 3.4.8-1
- Release python-cryptography 3.4.8

* Mon Sep 13 2021 Evgeni Golov - 3.1.1-1
- Release python-cryptography 3.1.1

* Wed Sep 08 2021 Evgeni Golov - 2.9.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 2.9.2-1
- Update to 2.9.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
