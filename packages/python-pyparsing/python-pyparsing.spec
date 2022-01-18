%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pyparsing

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.0.6
Release:        1%{?dist}
Summary:        Python parsing module

License:        MIT License
URL:            https://github.com/pyparsing/pyparsing/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jinja2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-railroad-diagrams
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jinja2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-railroad-diagrams


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
%doc README.rst examples/0README.html tests/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 18 2022 Odilon Sousa 3.0.6-1
- Update to 3.0.6

* Mon Sep 06 2021 Evgeni Golov - 2.4.7-2
- Build against Python 3.8

* Tue Apr 14 2020 Evgeni Golov 2.4.7-1
- Update to 2.4.7

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.6-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.4.6-1
- Update to 2.4.6

* Mon Nov 18 2019 Evgeni Golov - 2.4.5-1
- Initial package.
