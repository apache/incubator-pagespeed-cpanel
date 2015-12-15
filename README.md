# mod_pagespeed module for CPanel WHM

If you are using EasyApache4, please follow the below steps to install mod_pagespeed.
```
$> yum install rpm-build cpio ea-apache24-mod_version
$> wget https://github.com/Prajithp/cpanel/raw/master/EA4/ea-apache24-mod_pagespeed-1.9-32.11.src.rpm
$> rpmbuild --rebuild ea-apache24-mod_pagespeed-1.9-32.11.src.rpm
$> rpm -ivh /root/rpmbuild/RPMS/x86_64/ea-apache24-mod_pagespeed-1.9-32.11.x86_64.rpm
$> /etc/init.d/httpd restart
```

A custom module for CPanel WHM using CPanel Easy Framework - allows easy installation of mod_pagespeed via `/scripts/easyapache` on command line or through easyapache from WHM web console.

## Installation instructions

1. Clone the installation scripts onto your CPanel server:
```bash
$> /usr/local/cpanel/3rdparty/bin/git clone https://github.com/pagespeed/cpanel.git /var/cpanel/easy/apache/custom_opt_mods/Cpanel/
```

2. Create Speed.pm.tar.gz
```bash
$> cd /var/cpanel/easy/apache/custom_opt_mods/Cpanel/Easy
$> tar -zcvf Speed.pm.tar.gz pagespeed
$> rm -rf /var/cpanel/easy/apache/custom_opt_mods/Cpanel/Easy/pagespeed/
$> rm -rf /var/cpanel/easy/apache/custom_opt_mods/Cpanel/{.git,LICENSE,README.md}
```

3. Login into your cPanel WHM > EasyApache and look for "mod_pagespeed" option. Alternatively, you can run the easyapache installer from command line (`/scripts/easyapache`). Rebuild the Apache server, reboot it, and you're good to go!


## Configuring mod_pagespeed

The installation script will copy a default **pagespeed.conf** file into `/usr/local/apache/conf/` on your server. Please consult the following pages to customize your configuration:

- [mod_pagespeed module configuration](https://developers.google.com/speed/docs/mod_pagespeed/configuration)
- [configuring mod_pagespeed filters](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

For example of the different filters in action and detailed documentation for each, please see modpagespeed.com
