%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name redis

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        5.0.1
Release:        1%{?dist}
Summary:        Python client for Redis database and key-value store

License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-async-timeout >= 4.0.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 36.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-hiredis >= 1.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyopenssl = 20.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.26.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-async-timeout >= 4.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 36.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-hiredis >= 1.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata >= 1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyopenssl = 20.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.26.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions


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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 5.0.1-1
- Update to 5.0.1

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 4.3.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 4.3.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 4.3.4-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 4.3.4-1
- Update to 4.3.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.5.3-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.5.3-2
- Build against Python 3.8

* Thu Jun 04 2020 Evgeni Golov 3.5.3-1
- Update to 3.5.3

* Wed Mar 18 2020 Samir Jha 3.4.1-1
- Update to 3.4.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 3.1.0-1
- Initial package.
