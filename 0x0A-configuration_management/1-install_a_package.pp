# This Puppet manifest installs puppet-lint

package { 'puppet-lint':
  ensure   => '2.5.1',
  provider => 'gem',
 
}
