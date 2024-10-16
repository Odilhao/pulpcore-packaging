# Created by pyp2rpm-3.3.3
%global pypi_name dynaconf

Name:           python-%{pypi_name}
Version:        3.1.5
Release:        1%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 38.6.0

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-typing

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.1.5-1
- Release python-dynaconf 3.1.5

* Fri Mar 19 2021 Evgeni Golov 3.1.4-1
- Update to 3.1.4

* Thu Oct 29 2020 Evgeni Golov 3.1.2-1
- Update to 3.1.2

* Mon Sep 28 2020 Evgeni Golov 3.1.1-1
- Update to 3.1.1

* Tue Aug 25 2020 Evgeni Golov 3.1.0-1
- Update to 3.1.0

* Wed Mar 18 2020 Samir Jha 3.0.0-0.1.rc1
- Update to 3.0.0rc1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.2.2-1
- Update to 2.2.2

* Fri Dec 13 2019 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
