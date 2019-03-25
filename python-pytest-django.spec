# Created by pyp2rpm-3.3.2
%global pypi_name pytest-django

Name:           python-%{pypi_name}
Version:        3.4.8
Release:        1%{?dist}
Summary:        A Django plugin for pytest

License:        BSD-3-Clause
URL:            https://pytest-django.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(django-configurations) >= 2.0
BuildRequires:  python3dist(pathlib2)
BuildRequires:  python3dist(pytest) >= 3.6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.11.1
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx)

%description
 :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(django)
Requires:       python3dist(django-configurations) >= 2.0
Requires:       python3dist(pathlib2)
Requires:       python3dist(pytest) >= 3.6
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-rtd-theme)
%description -n python3-%{pypi_name}
 :target:

%package -n python-%{pypi_name}-doc
Summary:        pytest-django documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-django

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# tests yield error:
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
#%%check
#%%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_django
%{python3_sitelib}/pytest_django-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 3.4.8-1
- Initial package.
