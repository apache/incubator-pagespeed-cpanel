# mod_pagespeed module for CPanel WHM

A custom module for CPanel WHM using CPanel Easy Framework - allows easy installation of mod_pagespeed via `/scripts/easyapache` on command line or through easyapache from WHM web console.

## Installation instructions

Clone the installation scripts onto your CPanel server:

```
git clone git://github.com/pagespeed/cpanel.git /var/cpanel/easy/apache/custom_opt_mods/
```

That's it! Now you can install mod_pagespeed through CPanel:

* Run `/scripts/easyapache` from command line, or...
* Login into WHM and go to "EasyApache Update" and check the mod_pagespeed checkbox

## Configuring mod_pagespeed

The installation script will copy a default **pagespeed.conf** file into `/usr/local/apache/conf/` on your server. Please consult the following pages to customize your configuration:

- [mod_pagespeed module configuration](https://developers.google.com/speed/docs/mod_pagespeed/configuration)
- [configuring mod_pagespeed filters](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

For example of the different filters in action and detailed documentation for each, please see modpagespeed.com
