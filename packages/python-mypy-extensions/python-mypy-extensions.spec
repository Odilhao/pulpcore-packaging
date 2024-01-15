%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name mypy-extensions

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Type system extensions for programs checked with the mypy type checker

License:        MIT License
URL:            https://github.com/python/mypy_extensions
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/mypy_extensions-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n mypy_extensions-%{version}
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
%doc README.md
%{python3_sitelib}/__pycache__/mypy_extensions.*
%{python3_sitelib}/mypy_extensions.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/mypy_extensions-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> - 1.0.0-1
- Initial package.
