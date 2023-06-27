%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.28.0
Release:        1%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            https://pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Django >= 4.2.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-Django >= 4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PyYAML <= 6.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiodns <= 3.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiodns >= 3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiofiles < 23.2.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiofiles >= 22.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 3.8.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.8.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle <= 1.0.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle >= 1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-backoff < 2.2.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-backoff >= 2.1.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-click <= 8.1.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-click >= 8.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography < 41.0.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-filter <= 23.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-filter >= 23.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-guid <= 3.3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-guid >= 3.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-import-export < 3.3.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-import-export >= 2.9
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle <= 1.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle >= 1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-prometheus
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-storages
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-storages
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-storages >= 1.12.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-django-storages >= 1.13.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-djangorestframework <= 3.14.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.14.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields <= 1.0.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy < 1.5.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy >= 1.1.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-drf-nested-routers <= 0.93.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-drf-nested-routers >= 0.93.4
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-drf-spectacular = 0.26.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-dynaconf < 3.1.13
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-dynaconf >= 3.1.12
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gnupg <= 0.5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gnupg >= 0.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gunicorn <= 20.1.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-gunicorn >= 20.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jinja2 <= 3.1.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-jinja2 >= 3.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-naya <= 1.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-naya >= 1.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-distro <= 0.39b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-distro >= 0.38b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http <= 1.18.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http >= 1.17.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-django <= 0.39b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-django >= 0.38b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-wsgi <= 0.39b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-wsgi >= 0.38b0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-protobuf < 4.23.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-protobuf >= 4.21.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-psycopg <= 3.1.9
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-psycopg >= 3.1.8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pulp-glue < 0.20
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pulp-glue >= 0.18.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pygtrie <= 2.5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pygtrie >= 2.5
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-redis < 4.5.6
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-redis >= 4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools < 67.9.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 39.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-url-normalize <= 1.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-url-normalize >= 1.4.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-uuid6 <= 2024.1.1
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-uuid6 >= 2023.5.2
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-whitenoise < 6.5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-whitenoise >= 5.0
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-yarl < 1.9.3
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-yarl >= 1.8


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-Django >= 4.2.0
Conflicts:      %{?scl_prefix}python%{python3_pkgversion}-Django >= 4.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML <= 6.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-PyYAML >= 5.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiodns <= 3.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiodns >= 3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiofiles < 23.2.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiofiles >= 22.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp < 3.8.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-aiohttp >= 3.8.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle <= 1.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-asyncio-throttle >= 1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-backoff < 2.2.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-backoff >= 2.1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click <= 8.1.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-click >= 8.1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography < 41.0.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography >= 38.0.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-filter <= 23.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-filter >= 23.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-guid <= 3.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-guid >= 3.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-import-export < 3.3.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-import-export >= 2.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle <= 1.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-lifecycle >= 1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-prometheus
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-storages
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-storages
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-storages >= 1.12.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-django-storages >= 1.13.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework <= 3.14.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework >= 3.14.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields <= 1.0.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-djangorestframework-queryfields >= 1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy < 1.5.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-access-policy >= 1.1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-nested-routers <= 0.93.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-nested-routers >= 0.93.4
Requires:       %{?scl_prefix}python%{python3_pkgversion}-drf-spectacular = 0.26.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dynaconf < 3.1.13
Requires:       %{?scl_prefix}python%{python3_pkgversion}-dynaconf >= 3.1.12
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gnupg <= 0.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gnupg >= 0.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gunicorn <= 20.1.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-gunicorn >= 20.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jinja2 <= 3.1.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-jinja2 >= 3.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-naya <= 1.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-naya >= 1.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-distro <= 0.39b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-distro >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http <= 1.18.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-http >= 1.17.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-django <= 0.39b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-django >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-wsgi <= 0.39b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-opentelemetry-instrumentation-wsgi >= 0.38b0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf < 4.23.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-protobuf >= 4.21.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg <= 3.1.9
Requires:       %{?scl_prefix}python%{python3_pkgversion}-psycopg >= 3.1.8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-glue < 0.20
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pulp-glue >= 0.18.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygtrie <= 2.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-pygtrie >= 2.5
Requires:       %{?scl_prefix}python%{python3_pkgversion}-redis < 4.5.6
Requires:       %{?scl_prefix}python%{python3_pkgversion}-redis >= 4.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools < 67.9.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools >= 39.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-url-normalize <= 1.4.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-url-normalize >= 1.4.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uuid6 <= 2024.1.1
Requires:       %{?scl_prefix}python%{python3_pkgversion}-uuid6 >= 2023.5.2
Requires:       %{?scl_prefix}python%{python3_pkgversion}-whitenoise < 6.5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-whitenoise >= 5.0
Requires:       %{?scl_prefix}python%{python3_pkgversion}-yarl < 1.9.3
Requires:       %{?scl_prefix}python%{python3_pkgversion}-yarl >= 1.8


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
%{_bindir}/pulp-content
%{_bindir}/pulpcore-manager
%{_bindir}/pulpcore-worker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 27 2023 Odilon Sousa 3.28.0-1
- Update to 3.28.0

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-4
- Fix django-import-export requirement for Pulpcore 3.22

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-3
- Update python-backoff requirement for Pulpcore package

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-2
- Bump pulpcore release to fix one dependency requirement

* Mon Feb 13 2023 Odilon Sousa <osousa@redhat.com> - 3.22.2-1
- Release python-pulpcore 3.22.2

* Fri Feb 03 2023 Odilon Sousa <osousa@redhat.com> - 3.21.5-1
- Release python-pulpcore 3.21.5

* Mon Jan 23 2023 Patrick Creech <pcreech@redhat.com> - 3.21.4-1
- Release python-pulpcore 3.21.4

* Tue Sep 20 2022 Odilon Sousa 3.21.0-1
- Update to 3.21.0

* Wed Sep 14 2022 Odilon Sousa <osousa@redhat.com> - 3.18.10-1
- Release python-pulpcore 3.18.10

* Wed Aug 03 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.18.6-1
- Release python-pulpcore 3.18.6

* Thu May 26 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-2
- Adding a sed to change redis on requirements.txt, from ~= to >=

* Wed May 25 2022 Odilon Sousa <osousa@redhat.com> - 3.18.5-1
- Release python-pulpcore 3.18.5

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 3.18.4-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 29 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-3
- Fixing pulpcore requirements for djangorestframework

* Thu Apr 28 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-2
- Fixing the requirement for url-normalize

* Wed Apr 27 2022 Odilon Sousa <osousa@redhat.com> - 3.18.4-1
- Release python-pulpcore 3.18.4

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 3.17.3-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 3.17.3-1
- Release python-pulpcore 3.17.3

* Thu Dec 02 2021 Justin Sherrill <jsherril@redhat.com> 3.16.1-1
- update to 3.16.1

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 3.16.0-2
- Solving conflict with django-filter

* Mon Nov 15 2021 Odilon Sousa <osousa@redhat.com> - 3.16.0-1
- Release python-pulpcore 3.16.0

* Tue Oct 26 2021 Evgeni Golov - 3.15.2-4
- Also obsolete python3-pulpcore on EL7

* Wed Oct 20 2021 Evgeni Golov - 3.15.2-3
- Add provides for 'pulpcore'

* Wed Sep 29 2021 Evgeni Golov - 3.15.2-2
- Obsolete the old Python 3.6 package for smooth upgrade

* Wed Sep 08 2021 Evgeni Golov 3.15.2-1
- Update to 3.15.2

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.14.5-2
- Release python-pulpcore 3.14.5

* Wed Aug 25 2021 Odilon Sousa <osousa@redhat.com> - 3.14.5-1
- Release python-pulpcore 3.14.5

* Wed Aug 18 2021 Odilon Sousa <osousa@redhat.com> - 3.14.4-1
- Release python-pulpcore 3.14.4

* Mon Jul 26 2021 Justin Sherrill <jsherril@redhat.com> 3.14.3-1
- upgrade to 3.14.3

* Wed Jul 07 2021 Justin Sherrill <jsherril@redhat.com> 3.14.1-1
- update to 3.14.1

* Fri Jul 02 2021 Evgeni Golov - 3.14.0-1
- Release python-pulpcore 3.14.0

* Thu Jun 17 2021 Evgeni Golov - 3.13.0-2
- place the worker wrapper in libexec

* Fri Jun 11 2021 Evgeni Golov 3.13.0-1
- Update to 3.13.0

* Mon May 31 2021 Evgeni Golov - 3.11.2-1
- Release python-pulpcore 3.11.2

* Wed May 12 2021 Evgeni Golov 3.11.1-1
- Update to 3.11.1

* Wed Apr 28 2021 Justin Sherrill <jsherril@redhat.com> 3.11.0-2
- add patch for issue 8603

* Fri Mar 19 2021 Evgeni Golov 3.11.0-1
- Update to 3.11.0

* Wed Mar 03 2021 Brian Bouterse - 3.9.1-2
- Increase Pulp worker timeout to 300 seconds

* Fri Jan 22 2021 Evgeni Golov - 3.9.1-1
- Release python-pulpcore 3.9.1

* Mon Jan 11 2021 Evgeni Golov - 3.9.0-1
- Update to 3.9.0

* Mon Dec 21 2020 Evgeni Golov - 3.8.1-2
- Drop django-storages requirement, it was an oversight to add it

* Fri Dec 11 2020 Evgeni Golov 3.8.1-1
- Update to 3.8.1

* Tue Nov 03 2020 Evgeni Golov 3.7.3-1
- Update to 3.7.3

* Fri Oct 23 2020 Evgeni Golov - 3.7.2-1
- Release python-pulpcore 3.7.2

* Fri Oct 09 2020 Evgeni Golov - 3.7.1-3
- Bump dynaconf Requires to skip RCs

* Wed Oct 07 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.1-2
- Add libexec wrappers for gunicorn and rq

* Wed Sep 30 2020 Evgeni Golov 3.7.1-1
- Update to 3.7.1

* Mon Sep 07 2020 Evgeni Golov 3.6.3-1
- Update to 3.6.3

* Thu Sep 03 2020 Justin Sherrill <jsherril@redhat.com> 3.6.2-2
- add missing jinja2 dep

* Thu Sep 03 2020 Evgeni Golov 3.6.2-1
- Update to 3.6.2

* Tue Aug 25 2020 Evgeni Golov 3.6.0-1
- Update to 3.6.0

* Thu Jun 04 2020 Evgeni Golov 3.4.1-1
- Update to 3.4.1

* Fri May 08 2020 Evgeni Golov 3.3.1-1
- Update to 3.3.1

* Tue Apr 28 2020 Evgeni Golov 3.3.0-1
- Update to 3.3.0

* Wed Mar 18 2020 Samir Jha 3.2.1-1
- Update to 3.2.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.1-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 3.0.1-1
- Update to 3.0.1

* Fri Dec 13 2019 Evgeni Golov 3.0.0-1
- Update to 3.0.0

* Mon Nov 18 2019 Evgeni Golov - 3.0.0rc8-1
- Initial package.
