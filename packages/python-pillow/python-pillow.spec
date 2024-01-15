%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name Pillow
%global srcname pillow

Name:           %{?scl_prefix}python-%{srcname}
Version:        10.0.1
Release:        1%{?dist}
Summary:        Python Imaging Library (Fork)

License:        HPND
URL:            https://python-pillow.org
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-check-manifest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-coverage
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-defusedxml
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-furo
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-markdown2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-olefile
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-olefile
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-packaging
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pyroma
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest-timeout
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-check-manifest
Requires:       %{?scl_prefix}python%{python3_pkgversion}-coverage
Requires:       %{?scl_prefix}python%{python3_pkgversion}-defusedxml
Requires:       %{?scl_prefix}python%{python3_pkgversion}-furo
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markdown2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-olefile
Requires:       %{?scl_prefix}python%{python3_pkgversion}-olefile
Requires:       %{?scl_prefix}python%{python3_pkgversion}-packaging
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pyroma
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-cov
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest-timeout
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx >= 2.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-copybutton
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-inline-tabs
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-removed-in
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinxext-opengraph


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
%license LICENSE Tests/fonts/DejaVuSans/LICENSE.txt Tests/fonts/LICENSE.txt Tests/icc/LICENSE.txt
%doc README.md Tests/README.rst Tests/images/bmp/README.txt Tests/images/tga/common/readme.txt depends/README.rst src/thirdparty/raqm/README.md winbuild/README.md
%{python3_sitearch}/PIL
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> 10.0.1-1
- Update to 10.0.1

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 9.5.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 9.5.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 9.5.0-2
- Build against python 3.11

* Tue Jun 27 2023 Odilon Sousa - 9.5.0-1
- Initial package.
