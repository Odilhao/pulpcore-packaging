%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-importer

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.4.18
Release:        1%{?dist}
Summary:        Galaxy content importer

License:        Apache-2.0
URL:            https://github.com/ansible/galaxy-importer
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/galaxy_importer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-GitPython >= 3.1.20
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ansible-builder < 4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ansible-builder >= 1.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ansible-core
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ansible-lint <= 6.14.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-ansible-lint >= 6.2.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-attrs < 23
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-attrs >= 21.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-black >= 21.7b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bleach < 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bleach >= 3.3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bleach-allowlist < 2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-bleach-allowlist >= 1.0.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8 < 7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flake8 >= 5.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-markdown < 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-markdown >= 3.3.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyfakefs < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyfakefs >= 4.4.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest < 8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 7.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov >= 3.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mock < 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mock >= 3.8.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyyaml < 7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyyaml >= 5.4.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests < 3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.28.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-semantic-version < 3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-semantic-version >= 2.9.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-towncrier


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ansible-builder < 4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ansible-builder >= 1.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ansible-core
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ansible-lint <= 6.14.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-ansible-lint >= 6.2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs < 23
Requires:       %{?scl_prefix}python%{python3_pkgversion}-attrs >= 21.4.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bleach < 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bleach >= 3.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bleach-allowlist < 2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-bleach-allowlist >= 1.0.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flake8 < 7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flake8 >= 5.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markdown < 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markdown >= 3.3.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyyaml < 7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyyaml >= 5.4.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-requests >= 2.28.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-semantic-version < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-semantic-version >= 2.9.0


%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n galaxy_importer-%{version}
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
%license LICENSE galaxy_importer/utils/spdx_licenses.json galaxy_importer/utils/spdx_licenses.py
%doc README.md
%{python3_sitelib}/galaxy_importer
%{python3_sitelib}/galaxy_importer-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 0.4.18-1
- Update to 0.4.18

* Mon Nov 20 2023 Patrick Creech <pcreech@redhat.com> - 0.4.7-1
- Release python-galaxy-importer 0.4.7

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 0.4.6-3
- Obsolete python39 packages for a smooth upgrade

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.4.6-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 0.4.6-1
- Update to 0.4.6

* Tue Aug 23 2022 Odilon Sousa <osousa@redhat.com> - 0.4.5-1
- Release python-galaxy-importer 0.4.5

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.4.2-3
- Build against python 3.9

* Tue Feb 22 2022 Odilon Sousa <osousa@redhat.com> - 0.4.2-2
- Require /usr/bin/ansible

* Thu Feb 03 2022 Odilon Sousa <osousa@redhat.com> - 0.4.2-1
- Release python-galaxy-importer 0.4.2

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 0.4.1-1
- Release python-galaxy-importer 0.4.1

* Tue Oct 19 2021 Evgeni Golov - 0.4.0-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 0.4.0-1
- Update to 0.4.0

* Wed Sep 08 2021 Evgeni Golov - 0.3.2-3
- Correct non-SCL dependencies

* Mon Sep 06 2021 Evgeni Golov - 0.3.2-2
- Build against Python 3.8

* Wed May 12 2021 Evgeni Golov 0.3.2-1
- Update to 0.3.2

* Wed Apr 14 2021 Yanis Guenane - 0.3.0-3
- Add tar as a runtime Requires
- Manage /etc/galaxy-importer folder

* Wed Mar 31 2021 Evgeni Golov - 0.3.0-2
- Fix ansible-lint requires

* Wed Mar 31 2021 Evgeni Golov 0.3.0-1
- Update to 0.3.0

* Mon Feb 22 2021 Evgeni Golov - 0.2.15-1
- Release python-galaxy-importer 0.2.15

* Wed Dec 09 2020 Evgeni Golov - 0.2.12-1
- Release python-galaxy-importer 0.2.12

* Fri Nov 13 2020 Evgeni Golov - 0.2.11-1
- Release python-galaxy-importer 0.2.11

* Thu Nov 05 2020 Evgeni Golov 0.2.9-1
- Update to 0.2.9

* Mon Aug 31 2020 Evgeni Golov 0.2.8-1
- Update to 0.2.8

* Mon Aug 10 2020 Evgeni Golov 0.2.8-0.1.rc9
- Update to 0.2.8rc9

* Mon Jul 27 2020 Evgeni Golov 0.2.7-1
- Update to 0.2.7

* Mon Jul 27 2020 Evgeni Golov - 0.2.5-2
- Patch out Ansible and ansible-lint dependencies from the Python egg

* Tue Jun 23 2020 Evgeni Golov - 0.2.5-1
- Initial package.
