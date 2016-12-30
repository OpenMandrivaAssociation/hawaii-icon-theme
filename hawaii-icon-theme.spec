%define debug_package %{nil}

Summary:	Hawaii icon theme
Name:		hawaii-icon-theme
Version:	0.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
Source0:	https://github.com/hawaii-desktop/%{name}/archive/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
Requires:	hicolor-icon-theme
Requires:	adwaita-icon-theme
Requires:	faba-icon-theme
Requires:	captiva-icon-theme
%rename		hawaii-icon-themes

%track
prog %{name} = {
	url = https://github.com/hawaii-desktop/%{name}/archive/
	regex = "v(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Hawaii icon theme.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%{_iconsdir}/Hawaii
