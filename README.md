# mod_pagespeed module for CPanel WHM

A custom module for CPanel WHM using CPanel Easy Framework - allows easy installation of mod_pagespeed via `/scripts/easyapache` on command line or through easyapache from WHM web console.

## Installation instructions

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


## Configuring mod_pagespeed

The installation script will copy a default **pagespeed.conf** file into `/usr/local/apache/conf/` on your server. Please consult the following pages to customize your configuration:

- [mod_pagespeed module configuration](https://developers.google.com/speed/docs/mod_pagespeed/configuration)
- [configuring mod_pagespeed filters](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

For example of the different filters in action and detailed documentation for each, please see modpagespeed.com
