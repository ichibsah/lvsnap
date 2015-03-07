Summary:            A wrapper for managing LVM snapshots
Name:               lvsnap
Version:            0.9.1
Release:            1%{?dist}
License:            GPLv2+
Source:             %{name}-%{version}.tar.gz
URL:                https://github.com/brakarov/snappy
BuildArch:          noarch

BuildRequires:      gzip

Requires:			systemd
Requires:			coreutils
Requires:			grep
Requires:			sed
Requires:			lvm2
Requires:			rsync
Requires:			util-linux
Requires:			e2fsprogs
Requires:			bash >= 4.0

%description
The snappy program creates snapshots of partitions.
It can snapshot devices using LVM and rsync.

%prep
%autosetup -n %{name}

%build
gzip lvsnap.1

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 -d %{buildroot}/etc
install -m 755 -d %{buildroot}/etc/udev/rules.d
install -m 755 -d %{buildroot}/%{_mandir}/man1

install -m 555 -t %{buildroot}/%{_bindir} lvsnap
cp lvsnap.conf.example %{buildroot}/etc/lvsnap.conf
install -m 644 -t %{buildroot}/etc/udev/rules.d/ 99-hide-lvsnap-snapshots.rules 
chmod 644 %{buildroot}/etc/lvsnap.conf

cp lvsnap.1.gz %{buildroot}/%{_mandir}/man1/

%post
/usr/bin/udevadm trigger

%postun
/usr/bin/udevadm trigger

%files
%{_bindir}/lvsnap
%{_mandir}/man1/lvsnap.1.gz
/etc/lvsnap.conf
/etc/udev/rules.d/99-hide-lvsnap-snapshots.rules

%changelog
* Sat Mar 07 2015 Geert Braekmans <geert@localdomain>
- Initial release

