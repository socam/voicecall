Name:       voicecall-ui-reference
Summary:    Voice Call App
Version:    0.4.0
Release:    1
Group:      Communications/Telephony and IM
License:    Apache License, Version 2.0
URL:        http://github.com/nemomobile/voicecall-ui-reference
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(QtDeclarative)
Requires:  mapplauncherd-booster-qtcomponents

%description
Dialer Application for SOCAM

%prep
%setup -q -n %{name}-%{version}

%build
unset LD_AS_NEEDED
%qmake 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install

%files
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/autostart/voicecall-ui-prestart.desktop
%{_bindir}/voicecall-ui
%{_libdir}/systemd/user/voicecall-ui-prestart.service
/usr/share/applications/voicecall-ui.desktop
/usr/share/voicecall-ui/*




