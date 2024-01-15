%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name PyJWT
%global srcname pyjwt

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.8.0
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python

License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage = 5.0.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage = 5.0.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 3.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 3.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pre-commit
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest < 7.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest < 7.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-typing-extensions
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zope-interface
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-zope-interface


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage = 5.0.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 3.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest < 7.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 6.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx < 5.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx >= 4.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-rtd-theme
Requires:       %{?scl_prefix}python%{python3_pkgversion}-typing-extensions
Requires:       %{?scl_prefix}python%{python3_pkgversion}-zope-interface


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
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 2.8.0-1
- Update to 2.8.0

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.5.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.5.0-3
- Build against python 3.11

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.5.0-2
- Adding new dependency for python-pyjwt

* Tue Sep 20 2022 Odilon Sousa 2.5.0-1
- Update to 2.5.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.7.1-8
- Build against python 3.9

* Fri Nov 05 2021 Satoe Imaishi - 1.7.1-7
- Don't obsolete python 3.6 package and exclude files in bin

* Wed Sep 29 2021 Evgeni Golov - 1.7.1-6
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 22 2021 Evgeni Golov - 1.7.1-5
- Correct provides for Python 3.8

* Mon Sep 06 2021 Evgeni Golov - 1.7.1-4
- Build against Python 3.8

* Thu Aug 27 2020 Evgeni Golov - 1.7.1-3
- Obsolete python3-jwt

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.1-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 1.7.1-1
- Initial package.
