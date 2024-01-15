%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name gitdb

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        4.0.11
Release:        1%{?dist}
Summary:        Git Object Database

License:        BSD License
URL:            https://github.com/gitpython-developers/gitdb
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-smmap < 6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-smmap >= 3.0.1


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-smmap < 6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-smmap >= 3.0.1


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 4.0.11-1
- Update to 4.0.11

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.0.10-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.0.10-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.0.10-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 4.0.10-1
- Update to 4.0.10

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 4.0.9-2
- Build against python 3.9

* Mon Feb 07 2022 Odilon Sousa - 4.0.9-1
- Initial package.
