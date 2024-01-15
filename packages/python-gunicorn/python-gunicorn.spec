%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name gunicorn

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        21.2.0
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        MIT
URL:            https://gunicorn.org
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-eventlet
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-eventlet >= 0.24.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gevent
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gevent >= 1.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-packaging
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setproctitle
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tornado >= 0.2


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-eventlet >= 0.24.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gevent >= 1.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-importlib-metadata
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setproctitle
Requires:       %{?scl_prefix}python%{python3_pkgversion}-tornado >= 0.2


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
%doc README.rst docs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 21.2.0-1
- Update to 21.2.0

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-7
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 20.1.0-6
- Build against python 3.11

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-5
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 20.1.0-4
- Build against python 3.9

* Wed Sep 29 2021 Evgeni Golov - 20.1.0-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 20.1.0-2
- Build against Python 3.8

* Fri Jun 11 2021 Evgeni Golov 20.1.0-1
- Update to 20.1.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.0.4-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 20.0.4-1
- Update to 20.0.4

* Mon Nov 18 2019 Evgeni Golov - 20.0.0-1
- Initial package.
