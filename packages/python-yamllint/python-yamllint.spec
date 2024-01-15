%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name yamllint

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.33.0
Release:        1%{?dist}
Summary:        A linter for YAML files

License:        GPL-3.0-or-later
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-doc8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8-import-order
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pathspec >= 0.5.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyyaml
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rstcheck
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pathspec >= 0.5.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyyaml
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools


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
%{_bindir}/yamllint
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> - 1.33.0-1
- Initial package.
