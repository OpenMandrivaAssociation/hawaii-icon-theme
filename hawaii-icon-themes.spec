%define debug_package %{nil}

Summary:	Hawaii icon themes
Name:		hawaii-icon-themes
Version:	0.4.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
Source0:	https://github.com/hawaii-desktop/%{name}/archive/%{name}-%{version}.tar.gz
Source1:	hawaii-icon-themes.rpmlintrc
BuildRequires:	cmake
Requires:	hicolor-icon-theme
Requires:	adwaita-icon-theme
Requires:	faba-icon-theme
Requires:	captiva-icon-theme

%track
prog %{name} = {
	url = https://github.com/hawaii-desktop/%{name}/archive/
	regex = "v(__VER__)\.tar\.gz"
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
