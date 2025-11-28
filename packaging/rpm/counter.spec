Name:           file-counter
Version:        1.0
Release:        1
Summary:        A script to count files in /etc
BuildArch:      noarch
License:        GPL
Source0:        count_files.sh

%description
This package installs a script that counts files in /etc excluding directories and links.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/bin/count_files

%files
/usr/bin/count_files
