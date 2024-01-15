%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pyOpenSSL
%global srcname pyopenssl

Name:           %{?scl_prefix}python-%{srcname}
Version:        23.2.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library

License:        Apache License, Version 2.0
URL:            https://pyopenssl.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-cryptography = 40.0.0
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-cryptography = 40.0.1
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 5.2.0
BuildConflicts: %{?scl_prefix}python%{python3_pkgversion}-sphinx = 5.2.0.post0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography < 42
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-flaky
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pretend
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest >= 3.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-cryptography = 40.0.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-cryptography = 40.0.1
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-sphinx = 5.2.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-sphinx = 5.2.0.post0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography < 42
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-flaky
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pretend
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pytest >= 3.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-sphinx-rtd-theme


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
%{python3_sitelib}/OpenSSL
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Jan 15 2024 root <root@localhost> - 23.2.0-1
- Initial package.
