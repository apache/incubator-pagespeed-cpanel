%global ns_name ea-apache24
%global module_name mod_pagespeed

Summary: Apache module created by Google to help Make the Web Faster by rewriting web pages to reduce latency and bandwidth.
Name: ea-apache24-mod_pagespeed
Version: 1.9
Release: 32.11
License: Unknown
Group: System Environment/Daemons
URL: http://modpagespeed.com/
Source0: 456_pagespeed.conf
BuildRequires: wget
BuildRequires: cpio
Requires(pre): ea-apache24 ea-apache24-mod_version

# Suppres auto-provides for module DSO
%{?filter_provides_in: %filter_provides_in %{_libdir}/httpd/modules/.*\.so$}
%{?filter_setup}

%description
Apache module created by Google to help Make the Web Faster by rewriting web pages to reduce latency and bandwidth.

%prep
%if %{__isa_bits} == 64
wget -q -N -O  mod-pagespeed-stable.rpm https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_x86_64.rpm
%endif
%if %{__isa_bits} == 32
wget -q -N -O  mod-pagespeed-stable.rpm https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_i386.rpm
%endif

%build
rpm2cpio mod-pagespeed-stable.rpm  | cpio -idmv
%if %{__isa_bits} == 64
mv usr/lib64/httpd/modules/mod_pagespeed{,_ap24}.so .
%endif
%if %{__isa_bits} == 32
mv usr/lib/httpd/modules/mod_pagespeed{,_ap24}.so .
%endif
%{__strip} -g mod_pagespeed.so
%{__strip} -g mod_pagespeed_ap24.so

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_httpd_moddir}
install -m755 mod_pagespeed.so %{buildroot}%{_httpd_moddir}/
install -m755 mod_pagespeed_ap24.so %{buildroot}%{_httpd_moddir}/
# Install the config file
mkdir -p %{buildroot}%{_httpd_modconfdir}
install -m 644 %{SOURCE0} %{buildroot}%{_httpd_modconfdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0640,root,root,0755)
%attr(755,root,root)%{_httpd_moddir}/*.so
%config(noreplace) %{_httpd_modconfdir}/*.conf

%changelog
* Tue Dec 15 2015 Prajith <prajithpalakkuda@gmail.com> - 1.9-1
* Implement a new spec for cPanel
