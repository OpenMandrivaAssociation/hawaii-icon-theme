%define debug_package %{nil}

Summary:	Hawaii icon themes
Name:		hawaii-icon-themes
Version:	0.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-icon-themes.rpmlintrc
BuildRequires:	cmake

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Hawaii icon themes.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%{_iconsdir}/hawaii
%{_iconsdir}/elegant
