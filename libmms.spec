Name:       libmms
Version:    0.6.4
Release:    6%{?dist}
Summary:    Library for Microsoft Media Server (MMS) streaming protocol
License:    LGPLv2+
URL:        http://www.sf.net/projects/libmms

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool

Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:     0001-Remove-Requires-glib-2.0-since-libmms-no-longer-depe.patch
Patch2:     0003-Fix-build-if-strndup-is-missing.patch
Patch3:     0004-Patch-to-remove-redundant-comparison-in-file-mmsh.c.patch
Patch4:     0005-Avoid-possible-overflow-in-sprintf.patch
Patch5:     0006-Fix-possible-NULL-Pointer-deref-in-mmsh.c.patch
Patch6:     hide-internal-symbols.patch

%description
MMS is a proprietary streaming protocol used in Microsoft server products,
commonly used to stream WMV data.  You can encounter mms:// style URLs all over
the net, especially on news sites and other content-serving sites. Libmms allows
you to download content from such sites, making it easy to add MMS support to
your media applications.

%package devel
Summary:       Development package for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

# rpmlint fixes
chmod -x ChangeLog
find . -name "*.c" -exec chmod -x {} \;

%build
export CFLAGS="%{optflags}"
autoreconf -vif
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags} 


%install
%make_install
find %{buildroot}%{_libdir}/ -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog README*
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 0.6.4-6
- Add GCC build requirement.

* Wed Jul 04 2018 Simone Caronni <negativo17@gmail.com> - 0.6.4-5
- Update SPEC file.

* Sun Jun 05 2016 Simone Caronni <negativo17@gmail.com> - 0.6.4-4
- Update to latest git patches.
- Clean up SPEC file.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
