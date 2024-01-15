%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name django-lifecycle

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Declarative model lifecycle hooks

License:        MIT
URL:            https://github.com/rsinger86/django-lifecycle
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Django >= 2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging >= 21.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urlman >= 1.2.0


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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/django_lifecycle
%{python3_sitelib}/django_lifecycle-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 1.0.2-1
- Update to 1.0.2

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.0.0-2
- Build against python 3.11

* Tue Sep 20 2022 Odilon Sousa 1.0.0-1
- Update to 1.0.0

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.9.6-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Mon May 09 2022 Odilon Sousa <osousa@redhat.com> - 0.9.6-2
- Adding python-packaging as a dependency 

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 0.9.6-1
- Release python-django-lifecycle 0.9.6

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.9.3-2
- Build against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.9.3-1
- Release python-django-lifecycle 0.9.3

* Tue Oct 19 2021 Evgeni Golov - 0.9.1-3
- Obsolete the old Python 3.6 package for smooth upgrade

* Mon Sep 06 2021 Evgeni Golov - 0.9.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 0.9.1-1
- Update to 0.9.1

* Fri Oct 23 2020 Evgeni Golov - 0.8.0-1
- Release python-django-lifecycle 0.8.0

* Tue Aug 25 2020 Evgeni Golov - 0.7.7-1
- Initial package.
