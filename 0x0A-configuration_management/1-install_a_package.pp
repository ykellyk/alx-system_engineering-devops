#!/usr/bin/pup
# Install an especific version of flask (3.0.3)
package {'flask':
  ensure   => '3.0.3',
  provider => 'pip3'
}
