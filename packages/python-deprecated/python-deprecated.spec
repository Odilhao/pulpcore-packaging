%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name Deprecated
%global srcname deprecated

Name:           %{?scl_prefix}python-%{srcname}
Version:        1.2.14
Release:        1%{?dist}
Summary:        Python @deprecated decorator to deprecate old python classes, functions or methods

License:        MIT
URL:            https://github.com/tantale/deprecated
Source0:        https://files.pythonhosted.org/packages/source/D/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PyTest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PyTest-Cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bump2version < 1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tox
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wrapt < 2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wrapt >= 1.10


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-wrapt < 2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-wrapt >= 1.10


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
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


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.rst docs/source/license.rst
%doc README.md
%{python3_sitelib}/deprecated
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 1.2.14-1
- Update to 1.2.14

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.2.13-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.2.13-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.2.13-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa - 1.2.13-1
- Initial package.
