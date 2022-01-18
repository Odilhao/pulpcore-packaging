%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name requests

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        2.27.1
Release:        1%{?dist}
Summary:        Python HTTP for Humans

License:        Apache 2.0
URL:            https://requests.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-PySocks = 1.5.7
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-PySocks = 1.5.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PySocks >= 1.5.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PySocks >= 1.5.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-certifi >= 2017.4.17
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-chardet < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-chardet < 5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-chardet >= 3.0.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-chardet >= 3.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer >= 2.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer >= 2.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-idna < 3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-idna < 4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-httpbin = 0.0.7
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-mock
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-xdist
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-urllib3 < 1.27
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.21.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-win-inet-pton


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-PySocks = 1.5.7
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PySocks >= 1.5.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-certifi >= 2017.4.17
Requires:       %{?scl_prefix}python%{python3_pkgversion}-chardet < 5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-chardet < 5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-chardet >= 3.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-chardet >= 3.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer >= 2.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-charset-normalizer >= 2.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna < 3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna < 4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-idna >= 2.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 < 1.27
Requires:       %{?scl_prefix}python%{python3_pkgversion}-urllib3 >= 1.21.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-win-inet-pton


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
* Tue Jan 18 2022 Odilon Sousa 2.27.1-1
- Update to 2.27.1

* Wed Nov 17 2021 Evgeni Golov - 2.26.0-3
- Use charset-normalizer instead of chardet

* Tue Nov 16 2021 Evgeni Golov - 2.26.0-2
- Allow idna 4, 2.26 supports it

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 2.26.0-1
- Release python-requests 2.26.0

* Mon Sep 06 2021 Evgeni Golov - 2.25.1-2
- Build against Python 3.8

* Fri Mar 19 2021 Evgeni Golov 2.25.1-1
- Update to 2.25.1

* Mon Jul 20 2020 Evgeni Golov 2.24.0-1
- Update to 2.24.0

* Wed Mar 18 2020 Samir Jha 2.23.0-1
- Update to 2.23.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.22.0-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.22.0-1
- Initial package.
