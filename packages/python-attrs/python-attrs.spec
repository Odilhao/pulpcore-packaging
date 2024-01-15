%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name attrs

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        22.2.0
Release:        1%{?dist}
Summary:        Classes Without Boilerplate

License:        MIT
URL:            https://www.attrs.org/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-attrs
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-attrs
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-attrs
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cloudpickle
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cloudpickle
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage >= 5.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage-enable-subprocess
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-furo
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hypothesis
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hypothesis
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy < 0.990
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy < 0.990
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.971
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.971
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-myst-parser
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pympler
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pympler
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4.3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4.3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy-plugins
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy-plugins
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-towncrier
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zope-interface
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zope-interface


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cloudpickle
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cloudpickle
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage >= 5.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage-enable-subprocess
Requires:       %{?scl_prefix}python%{python3_pkgversion}-furo
Requires:       %{?scl_prefix}python%{python3_pkgversion}-hypothesis
Requires:       %{?scl_prefix}python%{python3_pkgversion}-hypothesis
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy < 0.990
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy < 0.990
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.971
Requires:       %{?scl_prefix}python%{python3_pkgversion}-mypy >= 0.971
Requires:       %{?scl_prefix}python%{python3_pkgversion}-myst-parser
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pympler
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pympler
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 4.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy-plugins
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-mypy-plugins
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-notfound-page
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinxcontrib-towncrier
Requires:       %{?scl_prefix}python%{python3_pkgversion}-towncrier
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zope-interface
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zope-interface


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
%license LICENSE docs/license.md
%doc README.md
%{python3_sitelib}/attr
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 22.2.0-1
- Update to 22.2.0

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 21.4.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 21.4.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 21.4.0-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 21.4.0-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa <osousa@redhat.com> - 21.4.0-1
- Release python-attrs 21.4.0

* Mon Sep 06 2021 Evgeni Golov - 21.2.0-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 21.2.0-1
- Update to 21.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 19.3.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 19.3.0-1
- Initial package.
