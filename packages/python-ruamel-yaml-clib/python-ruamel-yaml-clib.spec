%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml.clib
%global srcname ruamel-yaml-clib

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.2.8
Release:        1%{?dist}
Summary:        C version of reader, parser and emitter for ruamel

License:        MIT
URL:            https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


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
%license LICENSE
%doc README.rst
%{python3_sitearch}/ruamel
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 0.2.8-1
- Update to 0.2.8

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.2.7-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.2.7-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.2.7-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 0.2.7-1
- Update to 0.2.7

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.2.6-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.2.6-1
- Release python-ruamel-yaml-clib 0.2.6

* Wed Sep 08 2021 Evgeni Golov - 0.2.0-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.2.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.2.0-1
- Initial package.
