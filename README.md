# mod_pagespeed module for CPanel WHM

A custom module for CPanel WHM using CPanel Easy Framework - allows easy installation of mod_pagespeed via `/scripts/easyapache` on command line or through easyapache from WHM web console.

## Installation instructions

If you are using EasyApache4, please follow the below steps to install mod_pagespeed.
```
$> yum install rpm-build cpio ea-apache24-mod_version
$> wget https://github.com/Prajithp/cpanel/raw/master/EA4/ea-apache24-mod_pagespeed-latest-stable.src.rpm
$> rpmbuild --rebuild ea-apache24-mod_pagespeed-latest-stable.src.rpm
$> rpm -ivh /root/rpmbuild/RPMS/x86_64/ea-apache24-mod_pagespeed-latest-stable.src.rpm
$> /etc/init.d/httpd restart
```

1. Clone the installation scripts onto your CPanel server:
```bash
$> /usr/local/cpanel/3rdparty/bin/git clone https://github.com/pagespeed/cpanel.git /tmp/pagespeed/
```

2. Create Speed.pm.tar.gz
```bash
$> cd /tmp/pagespeed/Easy
$> tar -zcvf Speed.pm.tar.gz pagespeed
$> mkdir -p /var/cpanel/easy/apache/custom_opt_mods/Cpanel/Easy
$> mv Speed.pm Speed.pm.tar.gz -t /var/cpanel/easy/apache/custom_opt_mods/Cpanel/Easy/
$> cd && rm -rf /tmp/pagespeed
```

3. Login into your cPanel WHM > EasyApache and look for "mod_pagespeed" option. Alternatively, you can run the easyapache installer from command line (`/scripts/easyapache`). Rebuild the Apache server, reboot it, and you're good to go!

## Updating instructions

If you are using EasyApache3, run `easyapache` to upgrade mod_pagespeed to the
latest version.

If you are running EasyApache4, follow these steps to upgrade.

 - create file `/etc/rpm/macros.apache2` with the following contents

 ```
 %_httpd_mmn 20120211x8664
 %_httpd_apxs /usr/bin/apxs
 %_httpd_dir /etc/apache2
 %_httpd_bindir %{_httpd_dir}/bin
 %_httpd_modconfdir %{_httpd_dir}/conf.modules.d
 %_httpd_confdir %{_httpd_dir}/conf.d
 %_httpd_contentdir /usr/share/apache2
 %_httpd_moddir /usr/lib64/apache2/modules
 ```

 - then run the following commands

 ```bash
 rm -rf /root/rpmbuild/RPMS/x86_64/
 wget https://github.com/pagespeed/cpanel/raw/master/EA4/ea-apache24-mod_pagespeed-latest-stable.src.rpm
 rpmbuild --rebuild ea-apache24-mod_pagespeed-latest-stable.src.rpm
 rpm -Uvh /root/rpmbuild/RPMS/x86_64/ea-apache24-mod_pagespeed*.rpm
 /etc/init.d/httpd restart
 ```

## Configuring mod_pagespeed

The installation script will copy a default **pagespeed.conf** file into `/usr/local/apache/conf/` on your server. Please consult the following pages to customize your configuration:

- [mod_pagespeed module configuration](https://developers.google.com/speed/docs/mod_pagespeed/configuration)
- [configuring mod_pagespeed filters](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

For example of the different filters in action and detailed documentation for each, please see modpagespeed.com
