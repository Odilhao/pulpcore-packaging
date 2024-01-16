%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name bleach-whitelist

Name:           python-%{pypi_name}
Version:        0.0.11
Release:        7%{?dist}
Summary:        Curated lists of tags and attributes for sanitizing html

License:        BSD License
URL:            https://github.com/yourcelf/bleach-whitelist.git
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitelib}/bleach_whitelist
%{python3_sitelib}/bleach_whitelist-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 0.0.11-7
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 0.0.11-6
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 0.0.11-5
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.0.11-4
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 0.0.11-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 0.0.11-2
- Build against Python 3.8

* Mon Aug 10 2020 Evgeni Golov 0.0.11-1
- Update to 0.0.11

* Tue Jun 23 2020 Evgeni Golov - 0.0.10-1
- Initial package.
