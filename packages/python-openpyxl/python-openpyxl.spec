# Created by pyp2rpm-3.3.3
%global pypi_name openpyxl

Name:           python-%{pypi_name}
Version:        3.0.7
Release:        1%{?dist}
Summary:        A Python library to read/write Excel 2010 xlsx/xlsm files

License:        MIT
URL:            https://openpyxl.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-et-xmlfile

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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 3.0.7-1
- Update to 3.0.7

* Tue Aug 25 2020 Evgeni Golov 3.0.5-1
- Update to 3.0.5

* Mon Jul 20 2020 Evgeni Golov 3.0.4-1
- Update to 3.0.4

* Tue Apr 28 2020 Evgeni Golov - 3.0.3-1
- Initial package.
