#!/usr/bin/pup
# Specifically installs flask version 2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'gem'
}