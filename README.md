# mod_pagespeed module for CPanel WHM

A custom module for CPanel WHM using CPanel Easy Framework - allows easy installation of mod_pagespeed via `/scripts/easyapache` on command line or through easyapache from WHM web console.

## Installation instructions

Clone the installation scripts onto your CPanel server:

```
git clone git:// ... /var/cpanel/easy/apache/custom_opt_mods/
```

That's it! Now you can install mod_pagespeed through CPanel:

* Run `/scripts/easyapache` from command line, or...
* Login into WHM and go to "EasyApache Update" and check the mod_pagespeed checkbox

## Configuring mod_pagespeed

The installation script will copy a default **pagespeed.conf** file into `/usr/local/apache/conf/` on your server. Please consult the following pages to customize your configuration:

- [mod_pagespeed module configuration](https://developers.google.com/speed/docs/mod_pagespeed/configuration)
- [configuring mod_pagespeed filters](https://developers.google.com/speed/docs/mod_pagespeed/config_filters)

For example of the different filters in action and detailed documentation for each, please see modpagespeed.com

### License

Copyright (C) 2012-2013 [Prajith](http://www.prajith.in/install-mod_pagespeed-in-whmcpanel-using-easyapache/)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
